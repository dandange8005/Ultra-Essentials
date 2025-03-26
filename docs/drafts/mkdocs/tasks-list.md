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

## Best Practices

1. Keep task items concise and clear
2. Use consistent formatting within lists
3. Group related tasks together
4. Add context when necessary but keep it brief
5. Use nesting to show task hierarchy
6. Consider using icons for visual distinction
