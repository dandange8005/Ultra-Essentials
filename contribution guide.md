
## Within the DigEd Team

1. Request to join the repository as a contributor
2. Create your branch
3. Make your changes
4. Create a pull request
5. Wait for the pull request to be reviewed and merged
6. Delete your branch
7. Repeat

## Outside the DigEd Team

1. Fork the repository
2. Make your changes
3. Create a pull request
4. Wait for the pull request to be reviewed and merged
5. Repeat


## Steps to create a local environment

You don't have to do this but if you would like to run the project in your local environment by using MKdocs, you ware welcome to follow this instruction here to install Python and Material MKdocs.

1. Install python3
2. Install pip3
3. Install mkdocs-material
4. Run mkdocs new .
5. Run mkdocs serve
6. Start building the docs
7. create github action to build and deploy the docs

Here are the steps to setup the project


1. Clone the repo to your local machine

    You can use Github desktop to clone the repo to your local machine

    Or you can use the command line to clone the repo

    ```bash
    git clone ...
    ```

2. install python

    You will need to install python to run the mkdocs server locally

    ```bash
    brew install python
    ```

3. create a virtual environment

    This step would allow you to install the python libraries locally without affecting the global python installation
   
    ```bash
    python -m venv venv
    ```

4. active the virtual environment

    You will need to activate the virtual environment before installing the python libraries.

    ```bash
    source venv/bin/activate
    ```

5. install mkdocs-material

    Install the mkdocs-material library

    ```bash
    pip install mkdocs-material
    ```
6. install the plugins

    ```bash
    pip install mkdocs-git-revision-date-localized-plugin
    ...
    ```


## MkDocs Material


`mkdocs serve` - Start the live-reloading docs server.
`mkdocs build` - Build the documentation site.
`mkdocs -h` - Print help message and exit.
`mkdocs gh-deploy` - Deploy site to GitHub Pages.
`mkdocs -version` - Print the version of MkDocs.

creating a new project in the current directory
```bash
mkdocs new .
```

### Plugins used in the project

The project uses a number of plugins to enhance the functionality of the site. 

If you do happen to test the project locally, these plugins will need to be installed.

- [x] [mkdocs-git-revision-date-localized-plugin](https://github.com/timvink/)
- [x] [roamlinks](https://github.com/Jackiexiao/mkdocs-roamlinks-plugin)
- [x] [mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n)
- [ ] [MkDocs Awesome Pages Plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)