# Development guide

This steps allow you add new role to the collection.

1. Update version in `.release` file

2. Update pip dependencies:

    ```bash
    task dev:update-dependencies
    ```

3. Create a new role:

    ```bash
    task dev:create-role-role_name
    ```

4. Develop the role

5. Update genered files at 2nd step

6. Lint the collection

    ```bash
    task dev:lints
    ```

7. Test the role

    ```bash
    task dev:test-role-role_name
    ```

8. Commit the changes. Use one of the following prefixes:

> [!Note] This collection follows semantic versioning: `major.minor.patch`.

Minors:

- `feat` - Introduces a new feature.
- `delete` - Removes an existing feature.

Patches:

- `fix` - Resolves a bug.
- `perf` - Improves performance without changing behavior.

None:

- `revert` - Reverts a previous commit.
- `refactor` - Code changes that neither add a feature nor fix a bug.
- `test` - Adds new tests or updates existing ones.
- `style` - Code formatting changes (e.g., white-space, missing semi-colons) that don't affect functionality.
- `docs` - Updates or changes to documentation.
- `ci` - Changes to CI/CD configuration or scripts.
- `chore` - Maintenance tasks that do not modify source or test files.

> [!Important] Use `!` after a prefix to indicate a breaking change.

---
