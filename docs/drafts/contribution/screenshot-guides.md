# Screenshot Guidelines for Documentation

A comprehensive guide to creating, managing, and including screenshots in our MkDocs Material documentation.

---

## Quick Start Guide

=== "Direct Paste Method (Easiest)"

    1. **Capture** your screenshot with any tool
    2. **Paste directly** (Ctrl+V/Cmd+V) into the editor
    3. **Add alt text** when prompted for accessibility

    > *Note: Our system will automatically process, name, and place your screenshot*


=== "Recommended Method (Best Practice)"

    1. **Capture** your screenshot using our recommended tools
    2. **Save** following the naming convention: `page_section_description_v1.png`
    3. **Place** in `docs/assets/screenshots/`
    4. **Link** using: `![[assets/screenshots/page_section_description_v1.png|Alt text]]`


??? tip "Why follow these guidelines?"

    Consistent screenshot management helps:

    - **Find and update images** when the UI changes
    - **Maintain professional** documentation
    - **Ensure accessibility** for all users
    - **Keep our repository** clean and efficient


---

## Recommended Tools

Our documentation benefits from consistent, high-quality screenshots. These tools will help you capture perfect screenshots every time.

=== "macOS"
    **Shottr**: A powerful screenshot tool with annotation capabilities

    - Features: Scrolling capture, measurements, OCR, color picker
    - Download: [https://shottr.cc/](https://shottr.cc/)

    ![Shottr interface example](https://shottr.cc/assets/page-preview.jpg)


=== "Windows" 
    **ShareX**: Feature-rich screen capture and file sharing tool

    - Features: Region capture, screen recording, annotation tools
    - Download: [https://getsharex.com/](https://getsharex.com/)

    ![ShareX interface example](https://getsharex.com/img/ShareX_Screenshot.png)

## Screenshots in MkDocs Material

MkDocs Material supports several ways to include images in your documentation, but we recommend using Roam-style links for consistent referencing.

### Basic Syntax

```md
# Standard Markdown (not recommended)
![Alt text](path/to/image.png)

# Roam-style links (recommended)
![[assets/screenshots/filename.png|Alt text]]
```

### Advanced Usage

```md
# With size specifications
![[assets/screenshots/screenshot.png|300x200]]

# With alt text and size
![[assets/screenshots/screenshot.png|Alt text|300x200]]
```
### Benefits of Roam-style Links

1. ✅ No need to worry about relative paths
2. ✅ Works consistently across different documentation levels
3. ✅ Easier to maintain and refactor
4. ✅ Better integration with MkDocs
5. ✅ Automatic path resolution

### Best Practices

1. Always use the full path from the docs root
2. Include meaningful alt text using the pipe syntax
3. Keep image paths consistent with directory structure
4. Use size specifications when needed for consistency

---

## File Naming Convention

Consistent naming helps everyone find and update screenshots when needed.

### File Naming Pattern

```
<page>_<section>_<description>_<version>.png
```

### Examples

- `login_form_error_message_v1.png`
- `dashboard_widget_expanded_v2.png`
- `settings_api_keys_table_v1.png`

### Rules

1. Use lowercase letters and hyphens
2. Include version number if multiple iterations exist
3. Keep names descriptive but concise
4. Avoid spaces and special characters
5. Include context in the name (page/feature)

---

## Alt Text Guidelines

Alt text makes screenshots accessible to all users, including those using screen readers.

### Structure

```markdown
![[image_path|<action or context> - <specific description>]]
```

### Best Practices

1. Be specific and descriptive
2. Include important visual information
3. Keep it concise (125 characters max)
4. Describe the purpose, not the appearance
5. Include any visible text in the screenshot

### Examples

- ❌ Bad: `![[image.png|Screenshot]]`
- ❌ Bad: `![[image.png|Dashboard]]`
- ✅ Good: `![[image.png|Login form displaying validation error for incorrect password]]`
- ✅ Good: `![[image.png|Dashboard analytics panel showing monthly revenue chart]]`

---

## Screenshots checklist

Use this checklist to ensure your screenshots meet our documentation standards.

### Before Capturing

- [x] Determine if a screenshot is necessary for this section
- [x] Clear browser cache for consistent UI appearance
- [x] Use incognito/private browsing mode
- [x] Hide personal/sensitive information
- [x] Set browser zoom to 100%
- [x] Close unnecessary notifications and popups

### Capturing the Screenshot

- [x] Use the recommended tool:
    - Windows: [ShareX](https://getsharex.com/)
    - macOS: [Shottr](https://shottr.cc/)
- [x] Capture only what's necessary (not the entire screen)
- [x] Ensure text is readable
- [x] Check for visual clarity

### Saving the Screenshot

- [x] Follow the naming convention: `page_section_description_v1.png`
- [x] Use lowercase letters and hyphens
- [x] Keep the name descriptive but concise
- [x] Include version number (v1, v2, etc.)
- [x] Save in the correct location: `docs/assets/screenshots/`
- [x] Check file size (maximum 500KB)

### Adding Annotations (if needed)

- [x] Use consistent color scheme:
    - Red: Warnings/Errors
    - Green: Success/Confirmation
    - Blue: Information/Navigation
    - Yellow: Highlights/Important notes
- [x] Ensure annotations are clear and readable
- [x] Use consistent line thickness and arrow style
- [x] Add numbers for sequential steps (if applicable)

### Inserting in Documentation

- [x] Use Roam-style links: `![[assets/screenshots/filename.png|Alt text]]`
- [x] Include meaningful alt text (125 characters max)
- [x] Check that the image displays correctly
- [x] Verify the link path is correct

### Final Review

- [x] Image shows only what's needed
- [x] Text in image is readable
- [x] File size is optimized
- [x] No sensitive information is visible
- [x] Alt text accurately describes the image
- [x] Image properly integrates with surrounding text


## VSCode Plugins

- **Markdown All in One**: Useful for quick formatting and previewing

### Image processing

[Image](https://marketplace.visualstudio.com/items?itemName=n3rds-inc.image) { .external-link } - A powerful image processing tool for VSCode

