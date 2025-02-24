# Task Lists in MkDocs Material

Task lists (also known as checklist or todo lists) can be created using standard markdown syntax with some additional MkDocs Material enhancements.

## Basic Task List

```markdown
- [ ] Unchecked task item
- [x] Checked task item
- [ ] Another unchecked task
```

Which renders as:

- [ ] Unchecked task item
- [x] Checked task item
- [ ] Another unchecked task

## Nested Task Lists

```markdown
- [ ] Main task 1
    - [ ] Subtask 1.1
    - [x] Subtask 1.2
- [x] Main task 2
    - [x] Subtask 2.1
    - [ ] Subtask 2.2
```

- [ ] Main task 1
    - [ ] Subtask 1.1
    - [x] Subtask 1.2
- [x] Main task 2
    - [x] Subtask 2.1
    - [ ] Subtask 2.2

## Task Lists with Labels

```markdown
- [ ] ==Priority== Create project documentation
- [x] ~~Completed~~ Set up development environment
- [ ] **Important** Review pull requests
- [ ] *Optional* Add extra features
```

- [ ] ==Priority== Create project documentation
- [x] ~~Completed~~ Set up development environment
- [ ] **Important** Review pull requests
- [ ] *Optional* Add extra features

## Task Lists with Rich Content

```markdown
- [ ] Create user authentication system
    > Implement OAuth2 with support for multiple providers
    ```python
    def authenticate_user():
        pass
    ```
- [x] Update database schema
    - Changed user table structure
    - Added new indices
```

- [ ] Create user authentication system
    > Implement OAuth2 with support for multiple providers
    ```python
    def authenticate_user():
        pass
    ```
- [x] Update database schema
    - Changed user table structure
    - Added new indices

## Task Lists in Collapsible Blocks

```markdown
??? "Project Setup Tasks"
    - [ ] Initialize git repository
    - [ ] Set up virtual environment
    - [ ] Install dependencies
    - [ ] Configure settings

??? success "Completed Tasks"
    - [x] Create project structure
    - [x] Set up CI/CD pipeline
    - [x] Write initial tests
```

??? "Project Setup Tasks"
    - [ ] Initialize git repository
    - [ ] Set up virtual environment
    - [ ] Install dependencies
    - [ ] Configure settings

??? success "Completed Tasks"
    - [x] Create project structure
    - [x] Set up CI/CD pipeline
    - [x] Write initial tests

## Task Lists with Icons

```markdown
- [ ] :material-cloud-upload: Deploy to production
- [x] :material-test-tube: Run test suite
- [ ] :material-brush: Style components
- [x] :material-format-list-checks: Create task list
```

- [ ] :material-cloud-upload: Deploy to production
- [x] :material-test-tube: Run test suite
- [ ] :material-brush: Style components
- [x] :material-format-list-checks: Create task list

## Task Lists with Deadlines

```markdown
- [ ] Submit project proposal *(Due: 2024-03-01)*
- [ ] Complete first milestone *(Due: 2024-04-15)*
- [x] Team meeting ~~*(Due: 2024-02-20)*~~
```

- [ ] Submit project proposal *(Due: 2024-03-01)*
- [ ] Complete first milestone *(Due: 2024-04-15)*
- [x] Team meeting ~~*(Due: 2024-02-20)*~~


## Best Practices

1. Keep task items concise and clear
2. Use consistent formatting within lists
3. Group related tasks together
4. Add context when necessary but keep it brief
5. Use nesting to show task hierarchy
6. Consider using icons for visual distinction


## Custom Styling

Add to your `extra.css`:

```css
.task-list-item {
    list-style-type: none !important;
    margin-left: -1.5em;
}

.task-list-item input[type="checkbox"] {
    margin-right: 0.5em;
}

.task-list-control {
    position: relative;
    display: inline-block;
}
```