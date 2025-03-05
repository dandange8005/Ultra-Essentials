#!/usr/bin/env python3
"""
Screenshot Post-Processing Script

This script scans your MkDocs documentation and:
1. Finds embedded base64 images
2. Extracts them to properly named files
3. Updates the markdown with proper Roam-style links
4. Optimizes the images

Run it from your project root:
python scripts/process_screenshots.py

Optional arguments:
--dry-run: Show what would be changed without making changes
--path: Specific directory to process (default: docs)
"""

import os
import re
import sys
import base64
import argparse
from pathlib import Path
from datetime import datetime

# Try to import PIL for image optimization
try:
    from PIL import Image
    import io
    has_pillow = True
except ImportError:
    has_pillow = False
    print("Warning: Pillow is not installed. Images will not be optimized.")
    print("Install with: pip install pillow")

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Process screenshots in MkDocs documentation')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without making changes')
    parser.add_argument('--path', default='docs', help='Specific directory to process (default: docs)')
    parser.add_argument('--output-dir', default='assets/screenshots', help='Directory to save screenshots (relative to docs)')
    parser.add_argument('--max-width', type=int, default=1600, help='Maximum width for images (default: 1600)')
    parser.add_argument('--max-size', type=int, default=500, help='Maximum file size in KB (default: 500)')
    return parser.parse_args()

def generate_filename(md_file, alt_text, img_format):
    """Generate a filename based on the markdown file and content."""
    # Get the page name from the file path
    page_name = Path(md_file).stem.lower().replace(' ', '_')
    page_name = re.sub(r'[^a-z0-9_]', '', page_name)
    
    # Use alt text for description if available
    if alt_text:
        description = alt_text.lower().replace(' ', '_')
        description = re.sub(r'[^a-z0-9_]', '', description)[:20]
    else:
        # Create a timestamp-based description
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        description = f"screenshot_{timestamp[-6:]}"
    
    # Create the filename with a section placeholder (could be improved by parsing headers)
    filename = f"{page_name}_section_{description}_v1.{img_format}"
    
    return filename

def optimize_image(image_data, img_format, max_width, max_size_kb):
    """Optimize an image for web use."""
    if not has_pillow:
        return image_data
    
    try:
        img = Image.open(io.BytesIO(image_data))
        
        # Check if we need to resize
        width, height = img.size
        if width > max_width:
            ratio = max_width / width
            new_height = int(height * ratio)
            img = img.resize((max_width, new_height), Image.LANCZOS)
        
        # Save with appropriate options
        buffer = io.BytesIO()
        
        if img_format.lower() in ('jpg', 'jpeg'):
            img.save(buffer, format='JPEG', quality=85, optimize=True)
        elif img_format.lower() == 'png':
            img.save(buffer, format='PNG', optimize=True)
        else:
            # Unsupported format, return original
            return image_data
        
        optimized_data = buffer.getvalue()
        
        # Check if the optimization actually reduced the size
        if len(optimized_data) < len(image_data):
            return optimized_data
        
        # If not, return the original
        return image_data
    
    except Exception as e:
        print(f"Error optimizing image: {e}")
        return image_data

def process_markdown_file(file_path, args):
    """Process a single markdown file to extract and link images properly."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip files with no embedded images
    if 'data:image/' not in content:
        return 0
    
    # Find embedded base64 images
    pattern = r'!\[(.*?)\]\(data:image\/(\w+);base64,([^\)]+)\)'
    matches = re.findall(pattern, content)
    
    if not matches:
        return 0
    
    print(f"Found {len(matches)} embedded images in {file_path}")
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(args.path, args.output_dir)
    if not os.path.exists(output_dir) and not args.dry_run:
        os.makedirs(output_dir, exist_ok=True)
    
    # Track changes
    images_processed = 0
    new_content = content
    
    # Process each image
    for alt_text, img_format, base64_data in matches:
        # Generate filename
        filename = generate_filename(file_path, alt_text, img_format)
        filepath = os.path.join(output_dir, filename)
        
        # Decode the base64 data
        try:
            image_data = base64.b64decode(base64_data)
        except Exception as e:
            print(f"Error decoding base64 data: {e}")
            continue
        
        # Optimize the image
        if args.max_size > 0:
            optimized_data = optimize_image(image_data, img_format, args.max_width, args.max_size)
            size_before = len(image_data) / 1024
            size_after = len(optimized_data) / 1024
            savings = size_before - size_after
            
            if savings > 0:
                print(f"  Optimized {filename}: {size_before:.1f}KB → {size_after:.1f}KB (saved {savings:.1f}KB)")
        else:
            optimized_data = image_data
        
        # Save the image (unless dry run)
        if not args.dry_run:
            with open(filepath, 'wb') as f:
                f.write(optimized_data)
            print(f"  Saved to {filepath}")
        else:
            print(f"  Would save to {filepath}")
        
        # Create the replacement link
        rel_path = os.path.relpath(filepath, args.path)
        alt_part = f"|{alt_text}" if alt_text else ""
        new_link = f"![[{rel_path}{alt_part}]]"
        
        # Replace in content
        old_link = f"![{alt_text}](data:image/{img_format};base64,{base64_data})"
        new_content = new_content.replace(old_link, new_link)
        
        images_processed += 1
    
    # Save updated content (unless dry run)
    if images_processed > 0 and not args.dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path} with proper image links")
    
    return images_processed

def process_docs(args):
    """Process all markdown files in the docs directory."""
    print(f"Processing markdown files in {args.path}...")
    
    if args.dry_run:
        print("DRY RUN MODE: No changes will be made")
    
    # Find all markdown files
    md_files = []
    for root, _, files in os.walk(args.path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    print(f"Found {len(md_files)} markdown files")
    
    # Process each file
    total_processed = 0
    for file_path in md_files:
        processed = process_markdown_file(file_path, args)
        total_processed += processed
    
    print(f"Processed {total_processed} images across {len(md_files)} files")
    
    if args.dry_run and total_processed > 0:
        print("\nRun without --dry-run to apply these changes")

def main():
    """Main function."""
    args = parse_args()
    process_docs(args)

if __name__ == "__main__":
    main()