# Running a Local Dev Environment for MkDocs Material

This guide will help you set up your Visual Studio Code (VS Code) environment for contributing to the MkDocs Material project. 

## Prerequisites

Before you begin, make sure you have the following installed:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/)

## Clone the Repository

You have two options to clone the repository:

!!! GitHub Desktop:

    1. Download and install [GitHub Desktop](https://desktop.github.com/)
    2. Go to File > Clone Repository
    3. Select the repository from the list or enter the URL
    4. Choose your local path
    5. Click "Clone"

!!! Command Line

    1. Open your terminal
    2. Run the following command:

        ```bash
        git clone https://github.com/username/repository-name.git
        cd repository-name
        ```
        replace `username` and `repository-name` with the actual values

## Set Up Virtual Environment

1. Open the repository in VS Code
2. Open the terminal in VS Code
3. Run the following command to create a virtual environment:

    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
   
    - Windows:

        ```bash
        .\venv\Scripts\Activate
        ```

    - macOS/Linux:

        ```bash
        source venv/bin/activate
        ```
5. Install the required packages:
   
   Run the following command:

    ```bash
    pip install -r requirements.txt
    ```
6. You're all set! You can now run the development server:

    ```bash
    mkdocs serve --open
    ```
    If the browser doesn't open automatically, you can navigate to `http://localhost:8000` in your browser.

7. You can make changes to the documentation
8. Stop the server with `Ctrl + C` when done
9. Deactivate the virtual environment:

    ```bash
    deactivate
    ```


## Recommended VS Code Extensions

To enhance your development experience, we recommend the following extensions:

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
- [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [Image]()
- [Image Preview]()
- [YAML]()
