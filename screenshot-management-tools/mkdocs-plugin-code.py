"""
MkDocs Screenshot Manager Plugin

This plugin processes embedded screenshots and manages them according to naming conventions.
"""

import os
import re
import base64
import hashlib
from datetime import datetime
from pathlib import Path

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.utils import warning_filter

# Try to import PIL for image optimization
try:
    from PIL import Image
    import io
    has_pillow = True
except ImportError:
    has_pillow = False

class ScreenshotManagerPlugin(BasePlugin):
    """
    Plugin for managing screenshots in MkDocs.
    """
    
    config_scheme = (
        ('screenshot_path', config_options.Type(str, default='assets/screenshots')),
        ('auto_process', config_options.Type(bool, default=True)),
        ('optimize_images', config_options.Type(bool, default=True)),
        ('max_width', config_options.Type(int, default=1600)),
        ('max_size_kb', config_options.Type(int, default=500)),
        ('add_helper_script', config_options.Type(bool, default=True)),
    )
    
    def __init__(self):
        self.processed_images = 0
        self.total_size_saved = 0
    
    def on_config(self, config):
        """
        Set up the plugin when the config is loaded.
        """
        # Create the screenshot directory if it doesn't exist
        self.docs_dir = config['docs_dir']
        self.screenshot_dir = os.path.join(
            self.docs_dir, 
            self.config['screenshot_path']
        )
        os.makedirs(self.screenshot_dir, exist_ok=True)
        
        # Add helper script if enabled
        if self.config['add_helper_script']:
            if 'extra_javascript' not in config:
                config['extra_javascript'] = []
            
            # Check if custom JavaScript directory exists
            js_dir = os.path.join(self.docs_dir, 'assets', 'js')
            os.makedirs(js_dir, exist_ok=True)
            
            # Create the helper script
            js_path = os.path.join(js_dir, 'screenshot-helper.js')
            if not os.path.exists(js_path):
                with open(js_path, 'w') as f:
                    f.write(self._get_helper_script())
                
                # Add to config if not already there
                if 'assets/js/screenshot-helper.js' not in config['extra_javascript']:
                    config['extra_javascript'].append('assets/js/screenshot-helper.js')
            
            # Add CSS for helper
            if 'extra_css' not in config:
                config['extra_css'] = []
            
            css_dir = os.path.join(self.docs_dir, 'assets', 'css')
            os.makedirs(css_dir, exist_ok=True)
            
            css_path = os.path.join(css_dir, 'screenshot-helper.css')
            if not os.path.exists(css_path):
                with open(css_path, 'w') as f:
                    f.write(self._get_helper_css())
                
                # Add to config if not already there
                if 'assets/css/screenshot-helper.css' not in config['extra_css']:
                    config['extra_css'].append('assets/css/screenshot-helper.css')
        
        return config
    
    def on_page_markdown(self, markdown, page, config, files):
        """
        Process embedded images in markdown.
        """
        if not self.config['auto_process']:
            return markdown
        
        # Find embedded base64 images
        pattern = r'!\[(.*?)\]\(data:image\/(\w+);base64,([^\)]+)\)'
        
        def replace_match(match):
            """Replace base64 image with a proper link."""
            alt_text = match.group(1)
            img_format = match.group(2)
            base64_data = match.group(3)
            
            # Generate filename from page and content
            filename = self._generate_filename(page, alt_text, img_format)
            
            # Save the image
            filepath = self._save_base64_image(base64_data, img_format, filename)
            
            # Return the Roam-style link with alt text if provided
            rel_path = os.path.relpath(filepath, self.docs_dir)
            alt_part = f"|{alt_text}" if alt_text else ""
            
            return f"![[{rel_path}{alt_part}]]"
        
        # Replace all embedded images
        new_markdown = re.sub(pattern, replace_match, markdown)
        
        # Check if we've made any replacements
        if new_markdown != markdown:
            self.processed_images += len(re.findall(pattern, markdown))
        
        return new_markdown
    
    def on_post_build(self, config):
        """
        Show summary after build.
        """
        if self.processed_images > 0:
            print(f"\nScreenshot Manager: Processed {self.processed_images} embedded images")
            if self.total_size_saved > 0:
                saved_kb = self.total_size_saved / 1024
                print(f"Screenshot Manager: Optimized images, saving {saved_kb:.1f} KB")
    
    def _generate_filename(self, page, alt_text, img_format):
        """
        Generate a filename based on the page and content.
        """
        # Get page name from the page file
        page_name = os.path.splitext(os.path.basename(page.file.src_path))[0]
        page_name = re.sub(r'[^a-z0-9]', '_', page_name.lower())
        
        # Try to extract a section from the page content
        section_match = re.search(r'^#{2,3}\s+(.+)$', page.markdown, re.MULTILINE)
        if section_match:
            section = re.sub(r'[^a-z0-9]', '_', section_match.group(1).lower())
            section = re.sub(r'_+', '_', section).strip('_')[:20]
        else:
            section = "section"
        
        # Use alt text for description if available
        if alt_text:
            description = re.sub(r'[^a-z0-9]', '_', alt_text.lower())
            description = re.sub(r'_+', '_', description).strip('_')[:20]
        else:
            # Create a unique hash-based description
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            description = f"screenshot_{timestamp[-6:]}"
        
        # Create the filename
        filename = f"{page_name}_{section}_{description}_v1.{img_format}"
        
        return filename
    
    def _save_base64_image(self, base64_data, img_format, filename):
        """
        Save a base64 encoded image to file and optimize if necessary.
        """
        # Decode the base64 data
        image_data = base64.b64decode(base64_data)
        
        # Full path to save the image
        filepath = os.path.join(self.screenshot_dir, filename)
        
        # Original size
        original_size = len(image_data)
        
        # Optimize the image if PIL is available and optimization is enabled
        if has_pillow and self.config['optimize_images']:
            try:
                img = Image.open(io.BytesIO(image_data))
                
                # Check if we need to resize
                width, height = img.size
                max_width = self.config['max_width']
                
                if width > max_width:
                    ratio = max_width / width
                    new_height = int(height * ratio)
                    img = img.resize((max_width, new_height), Image.LANCZOS)
                
                # Save with appropriate options
                if img_format.lower() in ('jpg', 'jpeg'):
                    buffer = io.BytesIO()
                    img.save(buffer, format='JPEG', quality=85, optimize=True)
                    optimized_data = buffer.getvalue()
                    
                    # Only use optimized if it's actually smaller
                    if len(optimized_data) < original_size:
                        with open(filepath, 'wb') as f:
                            f.write(optimized_data)
                        self.total_size_saved += (original_size - len(optimized_data))
                    else:
                        with open(filepath, 'wb') as f:
                            f.write(image_data)
                
                elif img_format.lower() == 'png':
                    buffer = io.BytesIO()
                    img.save(buffer, format='PNG', optimize=True)
                    optimized_data = buffer.getvalue()
                    
                    # Only use optimized if it's actually smaller
                    if len(optimized_data) < original_size:
                        with open(filepath, 'wb') as f:
                            f.write(optimized_data)
                        self.total_size_saved += (original_size - len(optimized_data))
                    else:
                        with open(filepath, 'wb') as f:
                            f.write(image_data)
                
                else:
                    # Unsupported format for optimization
                    with open(filepath, 'wb') as f:
                        f.write(image_data)
            
            except Exception as e:
                print(f"Error optimizing image: {e}")
                # Fallback to saving without optimization
                with open(filepath, 'wb') as f:
                    f.write(image_data)
        else:
            # No PIL or optimization disabled
            with open(filepath, 'wb') as f:
                f.write(image_data)
        
        return filepath
    
    def _get_helper_script(self):
        """
        Generate the JavaScript helper for the documentation site.
        """
        return """
// MkDocs Screenshot Helper
document.addEventListener('DOMContentLoaded', function() {
    // Only run in edit mode or when there are textareas
    const isEditMode = window.location.pathname.includes('/edit/');
    const hasTextarea = document.querySelector('textarea') !== null;
    
    if (isEditMode || hasTextarea) {
        // Add paste event listener to textareas
        document.querySelectorAll('textarea').forEach(function(textarea) {
            textarea.addEventListener('paste', function(e) {
                // Check if paste contains image data
                const items = e.clipboardData.items;
                for (let i = 0; i < items.length; i++) {
                    if (items[i].type.indexOf('image') !== -1) {
                        // Show a helpful notification
                        showNotification('Screenshot detected! It will be processed automatically.');
                        break;
                    }
                }
            });
        });
    }
    
    // Function to show notification
    function showNotification(message, duration = 3000) {
        const notification = document.createElement('div');
        notification.className = 'screenshot-notification';
        notification.innerHTML = `
            <div class="screenshot-notification-content">
                <span class="screenshot-notification-icon">📷</span>
                <span class="screenshot-notification-message">${message}</span>
                <button class="screenshot-notification-close">&times;</button>
            </div>
        `;
        
        document.body.appendChild(notification);
        
        // Close button
        notification.querySelector('.screenshot-notification-close').addEventListener('click', function() {
            document.body.removeChild(notification);
        });
        
        // Auto-close after duration
        setTimeout(function() {
            if (notification.parentNode) {
                document.body.removeChild(notification);
            }
        }, duration);
    }
});
"""
    
    def _get_helper_css(self):
        """
        Generate the CSS for the helper UI.
        """
        return """
/* MkDocs Screenshot Helper Styles */
.screenshot-notification {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: var(--md-primary-fg-color, #2196f3);
    color: var(--md-primary-bg-color, white);
    padding: 12px;
    border-radius: 4px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    z-index: 1000;
    max-width: 300px;
    font-size: 14px;
    animation: fadeInUp 0.3s ease-out;
}

.screenshot-notification-content {
    display: flex;
    align-items: center;
}

.screenshot-notification-icon {
    margin-right: 8px;
    font-size: 18px;
}

.screenshot-notification-message {
    flex: 1;
}

.screenshot-notification-close {
    background: none;
    border: none;
    color: var(--md-primary-bg-color, white);
    cursor: pointer;
    font-size: 18px;
    padding: 0 0 0 8px;
    line-height: 1;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
"""