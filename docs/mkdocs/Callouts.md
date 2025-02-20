# Admonitions in MkDocs Material

Admonitions are attention-grabbing content blocks that help highlight important information in your documentation. They're perfect for warnings, notes, tips, and other types of callouts that should stand out from the regular content.

## Basic Usage

To add an admonition to your documentation, use the following syntax:

```markdown
!!! type "Optional Title"
    Content of your admonition goes here. 
    Make sure to indent the content.
```

Example

!!! type "Optional Title"
    Content of your admonition goes here. 
    Make sure to indent the content.

### Key Features

1. **Custom Titles**: You can customize the title or leave it empty to use the type's default title
2. **Multi-line Content**: Content can span multiple lines (with proper indentation)
3. **Markdown Support**: You can use Markdown formatting within admonitions

## Types of Admonitions

MkDocs Material provides several pre-styled admonition types, each designed for specific use cases:

### Information-related

```markdown
!!! note "Note"
    Use for general information and neutral observations.

!!! info "Info"
    Perfect for additional context and background information.

!!! abstract "Abstract"
    Ideal for summaries and high-level overviews.
```

### Guidance-related

```markdown
!!! tip "Tip"
    Share best practices and optimization suggestions.

!!! example "Example"
    Demonstrate practical applications and code samples.

!!! question "Question"
    Address common questions and provide clarification.
```

### Success-related

```markdown
!!! success "Success"
    Highlight positive outcomes and confirmations.
```

### Warning-related

```markdown
!!! warning "Warning"
    Alert users about potential issues or important considerations.

!!! danger "Danger"
    Emphasize critical warnings that require immediate attention.

!!! failure "Failure"
    Indicate common pitfalls or known issues.

!!! bug "Bug"
    Document known bugs or technical limitations.
```

### Other

```markdown
!!! quote "Quote"
    Include testimonials, citations, or important quotations.
```

## Advanced Features

### Collapsible Blocks

Create expandable/collapsible blocks using the `???` syntax:

```markdown
??? note "Expandable Note"
    This content is hidden by default.
    Click the arrow to expand.
```

Example

??? note "Expandable Note"
    This content is hidden by default.
    Click the arrow to expand.

### Nested Admonitions

You can nest admonitions within each other for complex documentation needs:

```markdown
!!! note "Outer Note"
    Regular note content

    !!! tip "Inner Tip"
        Nested tip content
```

Example

!!! note "Outer Note"
    Regular note content

    !!! tip "Inner Tip"
        Nested tip content

### Custom Callouts with CSS

!!! cu-red "Accessibility Note"
    This is a custom callout with a red background.

## Best Practices

1. **Choose Appropriate Types**: Select the admonition type that best matches your content's purpose
2. **Keep Content Focused**: Each admonition should contain a single, clear message
3. **Use Consistent Styling**: Maintain consistency in how you use admonitions throughout your documentation
4. **Don't Overuse**: Too many admonitions can overwhelm readers and reduce their effectiveness
5. **Indent Properly**: Always indent the content inside admonitions with 4 spaces or a tab

## Customization

You can customize the appearance of admonitions in your `mkdocs.yml`:

```yaml
theme:
  features:
    - admonition
  palette:
    scheme: default
    primary: indigo
    accent: indigo
```

## Available Admonition Types

- `note`
- `abstract`
- `info`
- `tip`
- `success`
- `question`
- `warning`
- `failure`
- `danger`
- `bug`
- `example`
- `quote`

For more advanced customization options and detailed documentation, visit the [MkDocs Material Admonitions Reference](https://squidfunk.github.io/mkdocs-material/reference/admonitions/).
