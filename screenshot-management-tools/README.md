# MkDocs Screenshot Management Tools

This package contains several tools to help manage screenshots in your MkDocs Material documentation:

1. **VSCode Extension**: For direct integration with your editor
2. **MkDocs Plugin**: For automatically processing screenshots during build
3. **Post-Processing Script**: For fixing existing documentation

## Installation & Setup

### 1. VSCode Extension

The VSCode extension is the most directly useful tool for your editing workflow. It:

- Intercepts pasted screenshots (with Ctrl+Shift+V)
- Automatically names and saves them following conventions
- Inserts proper Roam-style links in your markdown
- Provides a menu for generating screenshot filenames

To implement the extension:

1. Create a new directory for the extension
2. Copy the two files I created (`extension.js` and `package.json`)
3. Run `npm install` and then `vsce package` to create the VSIX file
4. Install it through VSCode's Extensions menu

```bash
# Install required tools
npm install -g @vscode/vsce

# Install dev dependencies
npm install

# Create the extension package
vsce package
```

Install the extension in VSCode:

   - Go to Extensions view (Ctrl+Shift+X)
   - Click the "..." menu and select "Install from VSIX..."
   - Select the .vsix file created in the previous step

After installation, you can:

   - Use Ctrl+Shift+V to paste screenshots with proper processing
   - Click the "Screenshot Helper" button in the status bar
   - Right-click in the editor to access screenshot functions

### MkDocs Plugin

The MkDocs plugin works during the build process to:

- Detect and extract any embedded screenshots
- Properly name and organize them
- Update markdown with the correct links
- Add helper UI to your documentation site

1. Copy the `mkdocs-plugin` directory to your project
2. Install the plugin:

```bash
# From your project root
pip install -e ./mkdocs-plugin
```

3. Add the plugin to your `mkdocs.yml`:

```yaml
plugins:
  - search
  - screenshot-manager:
      screenshot_path: assets/screenshots
      auto_process: true
      optimize_images: true
      max_width: 1600
      max_size_kb: 500
      add_helper_script: true
```

4. For image optimization, install Pillow:

```bash
pip install pillow
```

### Post-Processing Script

1. Copy the `process_screenshots.py` script to your project (e.g., to a `scripts` directory)
2. Make it executable:

```bash
chmod +x scripts/process_screenshots.py
```

3. Run it to process existing documentation:

```bash
# Do a dry run first to see what would be changed
python scripts/process_screenshots.py --dry-run

# Process all docs
python scripts/process_screenshots.py

# Process a specific directory
python scripts/process_screenshots.py --path docs/user-guide
```

## Usage

### VSCode Extension

1. **Paste a screenshot**: Use Ctrl+Shift+V to paste a screenshot from your clipboard. The extension will:
   - Save the image with a properly formatted name
   - Place it in the correct directory
   - Insert a Roam-style link with alt text

2. **Generate a filename**: Use the "Screenshot Helper" button in the status bar or right-click menu to generate a filename for a screenshot you're about to take.

### MkDocs Plugin

The plugin works automatically during the build process:

1. When MkDocs builds your site, it will scan for embedded base64 images
2. These images will be extracted, named, and saved to the specified directory
3. The markdown will be updated with proper Roam-style links
4. A small helper UI will be added to the documentation site

### Post-Processing Script

Run this script periodically to find and fix embedded screenshots:

```bash
python scripts/process_screenshots.py
```

## Best Practices

1. **Prefer the VSCode Extension** for day-to-day work
2. **Run the Post-Processing Script** periodically to catch any missed images
3. **Keep the MkDocs Plugin enabled** as a safety net

## Troubleshooting

### VSCode Extension Issues

- **Extension not working**: Make sure the extension is enabled for the workspace
- **Images not saving**: Check the output console for errors (View → Output, select "MkDocs Screenshot Helper")

### MkDocs Plugin Issues

- **Images not being processed**: Make sure the plugin is correctly configured in `mkdocs.yml`
- **Build errors**: Check if Pillow is installed for image optimization

### Post-Processing Script Issues

- **Script fails**: Try running with `--dry-run` to diagnose issues
- **Images not optimized**: Ensure Pillow is installed (`pip install pillow`)

## Customization

### VSCode Extension

Edit the `extension.js` file to customize:
- Naming patterns
- Storage location
- Keybindings (also in `package.json`)

### MkDocs Plugin

Edit the `plugin.py` file or adjust settings in `mkdocs.yml`:
```yaml
plugins:
  - screenshot-manager:
      # Custom settings here
```

### Post-Processing Script

Use command-line arguments to customize behavior:
```bash
python scripts/process_screenshots.py --help
```