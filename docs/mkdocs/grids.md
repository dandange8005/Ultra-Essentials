# Creating Grids layout in MkDocs

## Default Grid Layout

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

</div>


## Method 1
<div class="card-grid" markdown>
<div class="card" markdown>
### Feature 1
Feature description

[Learn More](feature1.md){ .card-button }
</div>

<div class="card" markdown>
### Feature 2
Feature description

[Learn More](feature2.md){ .card-button }
</div>

<div class="card" markdown>
### Feature 3
Feature description

[Learn More](feature3.md){ .card-button }
</div>
</div>

<style>
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    padding: 1rem;
}

.card {
    background: #f8f9fa;
    border-radius: 4px;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
}

.card-button {
    display: inline-block;
    margin-top: auto;
    padding: 0.5rem 1rem;
    background-color: var(--md-primary-fg-color);
    color: white!important;
    text-decoration: none;
    border-radius: 4px;
    text-align: center;
    transition: background-color 0.2s;
}

.card-button:hover {
    background-color: var(--md-primary-fg-color--dark);
}

.card-button:focus {
    outline: 2px solid var(--md-primary-fg-color);
    outline-offset: 2px;
}
</style>

## Method 2

Grid Layouts in MkDocs Material
[Previous content remains the same until the Feature Grid section, which is updated below...]
Feature Grid with Clickable Items
For highlighting features with icons that link to other pages:
htmlCopy<div class="feature-grid" markdown>

<div class="feature-item" markdown>
:material-rocket: 

### Fast

Quick setup and deployment

<a href="getting-started.md" class="overlay-link"></a>
</div>

<div class="feature-item" markdown>
:material-shield:

### Secure

Enterprise-grade security

<a href="security.md" class="overlay-link"></a>
</div>

<div class="feature-item" markdown>
:material-cog:

### Customizable

Flexible configuration

<a href="configuration.md" class="overlay-link"></a>
</div>

</div>

<style>
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    padding: 2rem;
}

.feature-item {
    display: block;
    text-align: center;
    padding: 1.5rem;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: transform 0.2s, box-shadow 0.2s;
    text-decoration: none;
    color: inherit;
}

.feature-item:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.feature-item .material-icons {
    font-size: 2.5rem;
    color: var(--md-primary-fg-color);
}

/* Optional: Add focus styles for accessibility */
.feature-item:focus {
    outline: 2px solid var(--md-primary-fg-color);
    outline-offset: 2px;
}
</style>