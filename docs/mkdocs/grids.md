# Grid Layouts in MkDocs Material

## Basic Grid Cards

The basic grid layout requires:
1. A container div with `grid cards` classes
2. Markdown enabled using the `markdown` attribute
3. List items as card content

```markdown
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Title Here__

    ---

    Card content goes here with regular markdown

    [:octicons-arrow-right-24: Call to Action](#)

</div>
```

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Title Here__

    ---

    Card content goes here with regular markdown

    [:octicons-arrow-right-24: Call to Action](#)

</div>

<!-- ### Breaking Down the Elements

- `.grid`: Creates the grid container
- `.cards`: Applies card styling
- `markdown`: Enables markdown processing inside the div
- `:material-icon:{ .lg .middle }`: Icon with classes for size and alignment
- `---`: Creates a divider line
- `__Text__`: Creates bold text for titles
- `[:octicons-arrow-right-24: Text](#)`: Creates a link with an icon -->

## Layout Variants

### Two-Column Grid

```markdown
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Column 1__

    Content for first column

-   :material-clock-fast:{ .lg .middle } __Column 2__

    Content for second column

</div>
```
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Column 1__

    Content for first column

-   :material-clock-fast:{ .lg .middle } __Column 2__

    Content for second column

</div>


### Three-Column Grid with Cards and No Dividers

```markdown
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg } __Card 1__
    
    First card content

-   :material-clock-fast:{ .lg } __Card 2__
    
    Second card content

-   :material-clock-fast:{ .lg } __Card 3__
    
    Third card content

</div>
```
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg } __Card 1__
    
    First card content

-   :material-clock-fast:{ .lg } __Card 2__
    
    Second card content

-   :material-clock-fast:{ .lg } __Card 3__
    
    Third card content

</div>


### Grid with Images

```markdown
<div class="grid cards" markdown>

-   ![Image 1](https://picsum.photos/600/400)

    __Image Card 1__
    
    Description for image 1

-   ![Image 2](https://picsum.photos/600/400)

    __Image Card 2__
    
    Description for image 2

</div>
```
<div class="grid cards" markdown>

-   ![Image 1](https://picsum.photos/600/400)

    __Image Card 1__
    
    Description for image 1

-   ![Image 2](https://picsum.photos/600/400)

    __Image Card 2__
    
    Description for image 2

</div>


<!-- ## Card Modifiers

### Icon Classes
- `.lg`: Large icon
- `.middle`: Vertically centers the icon
- `.inline`: Places icon inline with text

### Grid Classes
- `.cards`: Adds card styling with shadows and hover effects
- `.grid-no-gap`: Removes gap between grid items
- `.grid-stretch`: Makes all cards same height

## Custom Styling

You can add custom CSS to modify the grid layout:

```css
/* Customize card appearance */
.grid.cards > ul > li {
    border-radius: 4px;
    box-shadow: var(--md-shadow-z1);
}

/* Customize card hover state */
.grid.cards > ul > li:hover {
    box-shadow: var(--md-shadow-z2);
}

/* Customize grid columns */
.grid > ul {
    grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
}
``` -->

## Best Practices

1. Always include the `markdown` attribute when using markdown inside the grid
2. Use appropriate icon sizes (.lg for large, default for normal)
3. Keep content concise for better visual balance
4. Use consistent icon styles within the same grid
5. Include meaningful call-to-action links when needed
6. Test responsiveness on different screen sizes

## Common Icons

Material for MkDocs supports multiple icon sets:
- `:material-`: Material Design icons
- `:fontawesome-`: Font Awesome icons
- `:octicons-`: GitHub's Octicons
- `:simple-`: Simple Icons

Example icon usage:
```markdown
- :material-check-circle:{ .lg .middle }
- :fontawesome-regular-paper-plane:{ .lg }
- :octicons-repo-24:{ .middle }
```