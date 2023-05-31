
## Within the DigEd Team

1. Request to join the repository as a contributor
2. Create your own branch
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


## Steps to create the local environment

1. Install python3
2. Install pip3
3. Install mkdocs-material
4. Run mkdocs new .
5. Run mkdocs serve
6. Start building the docs
7. create github action to build and deploy the docs

## MKDOCS Material


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

The project uses a number of plugins to enhance the functionality of the site. The plugins are listed below:

- [x] [mkdocs-git-revision-date-localized-plugin](https://github.com/timvink/)
- [x] [roamlinks](https://github.com/Jackiexiao/mkdocs-roamlinks-plugin)
- [x] [mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n)
- [ ] [MkDocs Awesome Pages Plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)