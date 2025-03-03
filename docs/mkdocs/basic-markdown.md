# Basic Markdown Syntax

This page includes all the basic markdown syntax to get started with creating a document.

More about markdown syntax can be found [here](https://www.markdownguide.org/basic-syntax/) or you can use the [markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/) or GitHub's [mastering markdown](https://guides.github.com/features/mastering-markdown/)


## Paragraphs

```md
This is a paragraph.
```

This is a paragraph.

## Headings

```md
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
...
```

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

## Links

External links

```md
[Google.com](https://www.google.com/){.external-link}
```

[Google.com](https://www.google.com/){.external-link}

Internal links

```md
[[index]]
```

[[index]]

[[Callouts]]

## Images

Basic markdown syntax

```md
![alt text for the image](https://images.unsplash.com/photo-1739992115892-36453a241b5e?q=80&w=2512&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)
```


Images uploaded using external link

![alt text for the image](https://images.unsplash.com/photo-1739992115892-36453a241b5e?q=80&w=2512&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

## Lists

Unordered list

```md
- Item 1
- Item 2
- Item 3
```

- Item 1
- Item 2
- Item 3

Ordered list

```md
1. Item 1
2. Item 2
3. Item 3
```

1. Item 1
2. Item 2
3. Item 3

## Blockquotes

```md
> This is a blockquote
```

> This is a blockquote

## Tables

```md
| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Row 1    | Row 1    | Row 1    |
| Row 2    | Row 2    | Row 2    |
| Row 3    | Row 3    | Row 3    |
```

| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Row 1    | Row 1    | Row 1    |
| Row 2    | Row 2    | Row 2    |
| Row 3    | Row 3    | Row 3    |

??? example "Dos and Don'ts Example"

    | ✅ Do's | ❌ Don'ts |
    | ------- | -------- |
    | - item 1<br>- item 2<br>- item 3  | - don't item 1<br>- don't item 2<br>- don't item 3  |