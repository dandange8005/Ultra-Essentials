# Contributing Using GitHub Codespaces

This guide will help you set up and use GitHub Codespaces for contributing to our documentation. Codespaces provides a complete, configurable dev environment in the cloud, eliminating the need for local setup.

## Getting Started with Codespaces

### 1. Prerequisites

- A GitHub account
- Browser access to GitHub
- Repository access permissions

### 2. Creating a Codespace

1. Navigate to the repository on GitHub
2. Click the green "Code" button
3. Select the "Codespaces" tab
4. Click "Create codespace on main"

!!! tip "Resource Selection"
    You can choose different machine types for your codespace. For documentation work, the basic 2-core option is sufficient.

### 3. Working in Codespaces

Once your codespace launches, you'll see:
- VS Code in the browser
- A terminal window
- File explorer
- Source control view

## Setting Up the Documentation Environment

### 1. Install Required Packages

The following commands will be automatically run if you use our devcontainer configuration, but you can also run them manually:

```bash
# Install Python packages
pip install -r requirements.txt

# Verify installation
mkdocs --version
```

### 2. Start the Documentation Server

```bash
# Start the MkDocs server
mkdocs serve --dev-addr=0.0.0.0:8000
```

!!! note "Port Forwarding"
    Codespaces will automatically forward the port and provide you with a URL to view your documentation.

## Devcontainer Configuration

We provide a preconfigured development container. Here's our `.devcontainer/devcontainer.json`:

```json
{
    "name": "MkDocs Documentation",
    "image": "mcr.microsoft.com/devcontainers/python:3",
    "customizations": {
        "vscode": {
            "extensions": [
                "yzhang.markdown-all-in-one",
                "davidanson.vscode-markdownlint",
                "bierner.markdown-preview-github-styles"
            ]
        }
    },
    "postCreateCommand": "pip install -r requirements.txt",
    "forwardPorts": [8000],
    "portsAttributes": {
        "8000": {
            "label": "MkDocs Server",
            "onAutoForward": "notify"
        }
    }
}
```

## Workflow Tips

### 1. Branching and Changes

```bash
# Create a new branch
git checkout -b feature/new-documentation

# Make your changes
# Edit files using VS Code in browser

# Commit changes
git add .
git commit -m "Add new documentation section"

# Push changes
git push origin feature/new-documentation
```

### 2. Preview Changes

1. Click the "Ports" tab in Codespaces
2. Find the forwarded port (usually 8000)
3. Click the globe icon to open the preview in a new tab

### 3. Creating Pull Requests

1. Click the Source Control icon in the sidebar
2. Review your changes
3. Create a pull request directly from Codespaces
4. Fill in the PR template and submit

## Codespaces Features for Documentation

### 1. Live Preview

VS Code in Codespaces provides a live preview of Markdown files:
1. Open a .md file
2. Press `Ctrl+Shift+V` (or `Cmd+Shift+V` on Mac)
3. See rendered markdown in real-time

### 2. Integrated Terminal

Use the integrated terminal for MkDocs commands:
```bash
# Build the documentation
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

### 3. Extension Support

Recommended extensions (automatically installed):
- Markdown All in One
- markdownlint
- GitHub Markdown Preview

## Best Practices

1. **Resource Management**
   - Stop your codespace when not in use
   - Delete unused codespaces
   - Use lightweight machine types when possible

2. **Version Control**
   - Create feature branches for changes
   - Make regular commits
   - Keep PRs focused and small

3. **Documentation Standards**
   - Follow the project's style guide
   - Use relative links for internal references
   - Test all links and images

## Troubleshooting

### Common Issues

1. **Server Not Starting**
   ```bash
   # Check if port 8000 is in use
   lsof -i :8000
   # Try different port
   mkdocs serve --dev-addr=0.0.0.0:8001
   ```

2. **Package Installation Failures**
   ```bash
   # Upgrade pip
   python -m pip install --upgrade pip
   # Reinstall packages
   pip install -r requirements.txt
   ```

3. **Git Issues**
   ```bash
   # Reset Git credentials
   git config --global --unset credential.helper
   # Reconfigure Git
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

## Additional Resources

- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
- [VS Code in Browser Documentation](https://code.visualstudio.com/docs/remote/codespaces)
- [MkDocs Material Reference](https://squidfunk.github.io/mkdocs-material/reference/)

## Getting Help

If you encounter issues:
1. Check the GitHub Codespaces documentation
2. Look for similar issues in the repository
3. Ask for help in the project's discussion forum
4. Create a new issue with detailed information about your problem

!!! tip "Codespaces Timeout"
    Codespaces will automatically stop after 30 minutes of inactivity. Save your work regularly and commit changes to avoid losing progress.