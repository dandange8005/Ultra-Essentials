# Buttons in MkDocs Material

## Basic Button Types

### Regular Button
```markdown
[Regular button](#){.md-button}
```
[Regular button](#){.md-button}

### Primary Button
```markdown
[Primary button](#){.md-button .md-button--primary}
```
[Primary button](#){.md-button .md-button--primary}

## Buttons with Icons

### Leading Icons
```markdown
[:material-download: Download](#){.md-button}
[:material-email: Contact](#){.md-button}
[:material-github: GitHub](#){.md-button}
```
[:material-download: Download](#){.md-button}
[:material-email: Contact](#){.md-button}
[:material-github: GitHub](#){.md-button}

### Trailing Icons
```markdown
[Next :material-arrow-right:](#){.md-button}
[Upload :material-cloud-upload:](#){.md-button}
[Share :material-share:](#){.md-button}
```
[Next :material-arrow-right:](#){.md-button}
[Upload :material-cloud-upload:](#){.md-button}
[Share :material-share:](#){.md-button}

## Button Layouts

### Side by Side Buttons
```markdown
[First button](#){.md-button} [Second button](#){.md-button .md-button--primary}
```
[First button](#){.md-button} [Second button](#){.md-button .md-button--primary}

### Centered Button
```markdown
<div class="text-center" markdown>
[Center Button](#){.md-button}
</div>
```
<div class="text-center" markdown>
[Center Button](#){.md-button}
</div>

## Best Practices

1. Use descriptive button text
2. Add icons to improve visual understanding
3. Maintain consistent styling
4. Ensure adequate spacing between buttons
5. Use primary buttons sparingly
6. Test button layouts on mobile devices

## Common Patterns

### Call to Action
```markdown
[:material-rocket-launch: Get Started](#){.md-button .md-button--primary}
```

### Documentation Links
```markdown
[:material-book: Read the docs](#){.md-button} [:material-github: View source](#){.md-button}
```

### Form Submission
```markdown
[:material-send: Submit](#){.md-button .md-button--primary} [:material-cancel: Cancel](#){.md-button}
```