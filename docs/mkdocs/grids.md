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


