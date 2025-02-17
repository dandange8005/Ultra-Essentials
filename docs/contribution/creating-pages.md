# Creating New Pages in MkDocs

This guide will walk you through the process of creating new pages for your MkDocs documentation, including best practices and recommended patterns.

## File Naming Conventions

### Basic Rules

1. **Use lowercase letters**
   ```
   ✅ getting-started.md
   ❌ Getting-Started.md
   ```

2. **Use hyphens for spaces**
   ```
   ✅ installation-guide.md
   ❌ installation_guide.md
   ❌ installationGuide.md
   ```

3. **Keep names short but descriptive**
   ```
   ✅ user-auth.md
   ❌ detailed-user-authentication-and-authorization-guide.md
   ```

4. **Always use .md extension**
   ```
   ✅ config.md
   ❌ config.markdown
   ❌ config.txt
   ```

### Common Patterns

```text
# Standard pages
index.md              # Main landing page
getting-started.md    # Introduction page
installation.md       # Setup instructions
configuration.md      # Configuration guide
troubleshooting.md    # Problem-solving guide

# API documentation
api-overview.md
api-reference.md
api-authentication.md

# User guides
user-guide.md
admin-guide.md
developer-guide.md
```

## Page Structure

### Basic Page Template

```markdown
# Page Title

Brief introduction or overview of the page content.

## Overview

Main concepts or key points about the topic.

## Prerequisites

- Required knowledge
- Required software
- Required permissions

## Detailed Content

### First Section
Content for first section...

### Second Section
Content for second section...

## Related Information

- Link to related page
- Link to external resource
- Link to next steps

## See Also

- [Related Guide](related-guide.md)
- [External Resource](https://example.com)
```

## Directory Organization

### Recommended Structure

```
docs/
├── index.md                  # Home page
├── getting-started/          # Getting started section
│   ├── index.md             # Section landing page
│   ├── installation.md      # Installation guide
│   └── configuration.md     # Configuration guide
├── user-guide/              # User documentation
│   ├── index.md            # Guide overview
│   ├── basic-usage.md      # Basic usage
│   └── advanced.md         # Advanced features
└── reference/              # Reference documentation
    ├── index.md           # Reference overview
    ├── api.md            # API documentation
    └── configuration.md  # Configuration reference
```

## Navigation Setup

### mkdocs.yml Configuration

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Overview: getting-started/index.md
    - Installation: getting-started/installation.md
    - Configuration: getting-started/configuration.md
  - User Guide:
    - Overview: user-guide/index.md
    - Basic Usage: user-guide/basic-usage.md
    - Advanced Features: user-guide/advanced.md
  - Reference:
    - Overview: reference/index.md
    - API: reference/api.md
    - Configuration: reference/configuration.md
```

## Best Practices

### Content Organization

1. **Use Clear Hierarchy**
   - Main sections in root folder
   - Related content in subfolders
   - Index.md for section landing pages

2. **Logical Grouping**
   - Group related content together
   - Use consistent naming within groups
   - Maintain clear parent-child relationships

3. **URL Considerations**
   - Keep URLs short and meaningful
   - Use SEO-friendly names
   - Maintain consistent patterns

### File Management

1. **Assets Organization**
   ```
   docs/
   ├── assets/
   │   ├── images/
   │   ├── files/
   │   └── diagrams/
   ```

2. **Image Naming**
   ```
   ✅ user-login-flow.png
   ✅ dashboard-overview.png
   ❌ screenshot1.png
   ❌ img001.png
   ```

## Common Page Types

### Landing Pages (index.md)
```markdown
# Section Title

Brief overview of this section.

## In This Section

- [First Topic](./first-topic.md)
- [Second Topic](./second-topic.md)

## Quick Links

- [Common Tasks](./common-tasks.md)
- [Troubleshooting](./troubleshooting.md)
```

### API Documentation
```markdown
# API Reference

## Endpoint: /api/resource

### GET
Description of GET method...

### POST
Description of POST method...
```

### Tutorial Pages
```markdown
# Tutorial Title

## Prerequisites
What is needed before starting...

## Steps
1. First step...
2. Second step...

## Next Steps
What to do after completing...
```

## Tips for Writing

1. **Use Consistent Headers**
   - Start with H1 (#)
   - Use logical header progression
   - Don't skip header levels

2. **Include Navigation Aids**
   - Add "Previous/Next" links
   - Include "See Also" sections
   - Reference related documentation

3. **Maintain Readability**
   - Use short paragraphs
   - Include code examples
   - Add relevant images

## Common Mistakes to Avoid

❌ **Don't:**
- Use spaces in filenames
- Skip heading levels
- Create deeply nested folders
- Use inconsistent naming patterns
- Forget to update navigation

✅ **Do:**
- Use consistent naming
- Maintain clear structure
- Update navigation configs
- Include descriptive titles
- Add proper metadata

## Quick Reference

### Filename Patterns
```
# Feature documentation
feature-overview.md
feature-installation.md
feature-usage.md

# Version-specific docs
v1-guide.md
v2-guide.md

# Role-specific docs
admin-guide.md
user-guide.md
developer-guide.md
```

### Standard Sections
```markdown
# Title
## Overview
## Prerequisites
## Installation
## Configuration
## Usage
## Troubleshooting
## FAQ
## Reference
```

Remember: Good organization and consistent naming make documentation more maintainable and user-friendly.

!!! tip "Testing Links"
    Always test your internal links after creating new pages to ensure proper navigation.