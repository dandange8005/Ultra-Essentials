# Images in MkDocs Material

Images are essential for creating engaging and informative documentation. MkDocs Material provides several ways to include and customize images in your documentation.

## Basic Image Syntax

To add an image to your documentation, use the standard Markdown syntax:

```markdown
![Alt text](path/to/image.png)
```

### Key Features

1. **Alt Text**: Provide descriptive alt text for accessibility
2. **Relative Paths**: Use relative paths from your docs directory
3. **Multiple Formats**: Support for common image formats (PNG, JPG, GIF, SVG)

## Image Organisation

### Recommended Directory Structure

```
mkdocs-project/
├── docs/
│   ├── assets/
│   │   ├── screenshots/
│   │   ├── images/
│   │   └── files/
│   └── index.md
└── mkdocs.yml
```

### Path References

```markdown
# Absolute path from docs directory
![Logo](/images/logo.png)

# Relative path from current file
![Screenshot](../images/screenshots/feature.png)
```

## Advanced Features

### Image Alignment

Use HTML attributes to align images:

```markdown
![Centered Image](image.png){: .center}

![Right-aligned Image](image.png){: align=right}

![Left-aligned Image](image.png){: align=left}
```

### Image Sizing

Control image dimensions using attributes:

```markdown
![Small Image](image.png){: style="width:200px"}

![Half-width Image](image.png){: style="width:50%"}

![Custom Size](image.png){: width="300" height="200"}
```

### Image Captions

Add captions to your images:

```markdown
<figure>
    ![Screenshot](image.png)
    <figcaption>Figure 1: Description of the image</figcaption>
</figure>
```

## Best Practices

1. **Optimise Images**
    - Compress images before adding to documentation
    - Use appropriate file formats (PNG for screenshots, JPG for photos)
    - Consider using SVG for diagrams and icons

2. **Descriptive Alt Text**
    ```markdown
    # Good
    ![Dashboard showing user statistics and active sessions](dashboard.png)

    # Bad
    ![Dashboard](dashboard.png)
    ```

## Advanced Configuration

### Image Gallery Example

Create an image gallery using CSS Grid:

```markdown
<div class="image-grid">
    ![Image 1](img1.png)
    ![Image 2](img2.png)
    ![Image 3](img3.png)
</div>
```

```css
.image-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    padding: 1rem;
}
```

## Common Issues and Solutions

### Broken Images

```markdown
# Check if path is correct
![Image](./path/to/image.png)

# Use forward slashes, even on Windows
![Image](images/screenshot.png)
```

### Large Images

```markdown
# Resize large images
![Large Image](big-image.png){: style="width:800px;max-width:100%"}

# Use HTML for more control
<img src="big-image.png" alt="Large Image" style="width:100%;max-width:800px">
```

### SVG Handling

```markdown
# Inline SVG
<svg width="100" height="100">
    <!-- SVG content -->
</svg>

# SVG as image
![SVG Image](diagram.svg){: style="background:white"}
```

## Tips for Documentation Authors

1. **Image Naming**
      * Use descriptive, kebab-case names: `user-dashboard-overview.png`
      * Include dimensions if relevant: `hero-banner-1200x600.png`

2. **Version Control** 
      * Consider using Git LFS for large images
      * Keep image sizes reasonable (< 500KB per image)
      * Document image dimensions in a separate README

3. **Accessibility**
      * Always include meaningful alt text
      * Provide text alternatives for complex diagrams
      * Consider color-blind users when creating charts

For more advanced features and detailed documentation, visit the [MkDocs Material Images Reference](https://squidfunk.github.io/mkdocs-material/reference/images/).







