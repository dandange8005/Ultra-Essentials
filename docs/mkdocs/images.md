# Images in MkDocs Material

Images are essential for creating engaging and informative documentation. MkDocs Material provides several ways to include and customize images in your documentation.

## Basic Image Syntax

To add an image to your documentation, use the standard Markdown syntax:

```markdown
![Alt text](https://unsplash.it/500/300?random)
```
![Alt text](https://unsplash.it/500/300?random)

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

#### Direct name reference
```md
![Alt text](accommodation-status.png)
```
![Alt text](accommodation-status.png)

#### Relative path reference
```md
![Alt text](../assets/images/Cardiff-Logo-Red-Inversed.svg)
```
![Alt text](../assets/images/Cardiff-Logo-Red-Inversed.svg)

#### Direct path reference
```md
![Alt text](/assets/images/Cardiff-Logo-Red-Inversed.svg)
```
![Alt text](/assets/images/Cardiff-Logo-Red-Inversed.svg)

#### URL reference
```md
![Alt text](https://unsplash.it/500/300?random)
```
![Alt text](https://unsplash.it/500/300?random)

## Image Sizing

Control image dimensions using attributes:

```md
![Small Image](image.png){ width=300 }

![Half-width Image](image.png){ width=50% }

![Custom Size](image.png){ width=200 height=100 }
```

## Image Alignment

Use HTML attributes to align images:

```markdown

![Right-aligned Image](image.png){align=right}

![Left-aligned Image](image.png){align=left}
```

![Right-aligned Image](https://unsplash.it/200/200){align=right}

Right-aligned Image:

<br clear="all" />


![Left-aligned Image](https://unsplash.it/200/200){align=left}

Left-aligned Image:

<br clear="all" />


### Image Captions

Add captions to your images:

```markdown
<figure markdown="span">
  ![Image title](https://dummyimage.com/600x400/){ width="300" }
  <figcaption>Image caption</figcaption>
</figure>
```
<figure markdown="span">
    ![image](https://unsplash.it/700/400)
    <figcaption>Figure 1: Description of the image</figcaption>
</figure>


## Best Practices

1. **Image Naming**
    - Use descriptive names: `dashboard-screenshot.png`
    - Avoid special characters and spaces
    - Use lowercase and kebab-case
2. **Optimise Images**
    - Compress images before adding to documentation
    - Use appropriate file formats (PNG for screenshots, JPG for photos)
    - Consider using SVG for diagrams and icons
3. **Accessibility**
   
      - Always include meaningful alt text
           ```markdown
           # Good
           ![Dashboard showing user statistics and active sessions](dashboard.png)

           # Bad
           ![Dashboard](dashboard.png)
           ```
      - Provide text alternatives for complex diagrams
      - Consider color-blind users when creating charts
      - Keep image sizes reasonable (< 500KB per image)


For more advanced features and detailed documentation, visit the [MkDocs Material Images Reference](https://squidfunk.github.io/mkdocs-material/reference/images/){.external-link}.







