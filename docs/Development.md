# Development guide

This steps allow you add new role to the collection.

1. Update pip dependencies:

    ```bash
    task dev:update-dependencies
    ```

2. Create a new role:

    ```bash
    task dev:create-role-role_name
    ```

3. Develop the role

4. Update genered files at 2nd step

5. Lint the collection

    ```bash
    task dev:lints
    ```

6. Test the role

    ```bash
    task dev:test-role-role_name
    ```

7. Commit the changes. Use one of the following prefixes:

> [!Note] This collection follows semantic versioning: `major.minor.patch`.

- `feat` (minor) - Introduces a new feature.
- `delete` (minor) - Removes an existing feature.

- `fix` (patch) - Resolves a bug.
- `perf` (patch) - Improves performance without changing behavior.

- `revert` (none) - Reverts a previous commit.
- `refactor` (none) - Code changes that neither add a feature nor fix a bug.
- `test` (none) - Adds new tests or updates existing ones.
- `style` (none) - Code formatting changes (e.g., white-space, missing semi-colons) that don't affect functionality.
- `docs` (none) - Updates or changes to documentation.
- `ci` (none) - Changes to CI/CD configuration or scripts.
- `chore` (none) - Maintenance tasks that do not modify source or test files.

> [!Important] Use `!` after a prefix to indicate a breaking change.

---
