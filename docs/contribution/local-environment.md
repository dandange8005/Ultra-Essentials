# Running a local environment

This guide will help you set up a local development environment for contributing to our documentation project. Follow these steps to get the project running on your machine.

## Prerequisites

Before you begin, ensure you have:

- Git installed on your machine
- A code editor (VS Code, Sublime Text, etc.)
- Terminal/Command Prompt access
- GitHub account

## Setting Up Your Local Environment

### 1. Clone the Repository

You have two options to clone the repository:

**Option 1: Using GitHub Desktop**
1. Open GitHub Desktop
2. Go to File > Clone Repository
3. Select the repository from the list or enter the URL
4. Choose your local path
5. Click "Clone"

**Option 2: Using Command Line**
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

### 2. Install Python

**macOS (using Homebrew)**
```bash
brew install python
```

**Windows**
1. Download Python installer from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. Check "Add Python to PATH" during installation

**Linux**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

Verify installation:
```bash
python --version
pip --version
```

### 3. Set Up Virtual Environment

Creating a virtual environment helps isolate project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

Your prompt should change to indicate the virtual environment is active.

### 4. Install Required Packages

Install MkDocs Material and required plugins:

```bash
# Install MkDocs Material
pip install mkdocs-material

# Install required plugins
pip install mkdocs-git-revision-date-localized-plugin
pip install mkdocs-glightbox
pip install pillow cairosvg

# Save dependencies to requirements.txt
pip freeze > requirements.txt
```

## Running the Documentation Locally

### Basic Commands

```bash
# Start the local server
mkdocs serve

# Build the static site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

Access your local documentation at `http://127.0.0.1:8000`

### Development Workflow

1. Start the local server:
```bash
mkdocs serve
```

2. Make changes to your documentation
3. View changes in real-time at `http://127.0.0.1:8000`
4. Stop the server with `Ctrl + C` when done

## Project Structure

```
mkdocs-project/
├── docs/
│   ├── index.md
│   ├── getting-started.md
│   └── ...
├── .github/
│   └── workflows/
│       └── ci.yml
├── mkdocs.yml
├── requirements.txt
└── README.md
```

## Configuration

### Basic mkdocs.yml Setup

```yaml
site_name: Project Documentation
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.highlight

plugins:
  - search
  - git-revision-date-localized

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

## GitHub Actions Deployment

Create `.github/workflows/ci.yml`:

```yaml
name: ci 
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: mkdocs gh-deploy --force
```

## Common Issues and Solutions

### Virtual Environment Issues

If you see "command not found" after activating virtual environment:
```bash
# Reinstall packages in virtual environment
pip install -r requirements.txt
```

### Port Already in Use

If port 8000 is occupied:
```bash
# Use a different port
mkdocs serve -a localhost:8001
```

### Build Failures

If `mkdocs build` fails:
1. Check syntax in markdown files
2. Verify all linked files exist
3. Ensure mkdocs.yml is properly formatted

## Best Practices

1. **Always work in virtual environment**
   - Activate before starting work
   - Deactivate when done: `deactivate`

2. **Keep dependencies updated**
   ```bash
   pip install --upgrade mkdocs-material
   pip freeze > requirements.txt
   ```

3. **Test locally before pushing**
   - Run `mkdocs build` to check for errors
   - Preview all changes in local server

## Additional Resources

- [MkDocs Documentation](https://www.mkdocs.org/user-guide/writing-your-docs/)
- [Material for MkDocs Reference](https://squidfunk.github.io/mkdocs-material/reference/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)

## Getting Help

If you encounter any issues:
1. Check the [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
2. Search existing GitHub issues
3. Create a new issue if needed

Remember to deactivate your virtual environment when you're done:
```bash
deactivate
```