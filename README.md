# Ansible Collection - internal.linux_base

This collection offers a set of roles for managing Linux systems:

- The users role manages user accounts.
- The packages role handles package management.
- The firewalld role manages the firewalld service.
- The cockpit role manages the cockpit service.

## Install dependencies

1. Install Go task. [Installation guide](https://taskfile.dev/installation/)

2. Create a virtual environment and activate it:

    ```bash
    ls .venv || python3 -m venv .venv
    [ -n VIRTUAL_ENV ] && source .venv/bin/activate
    ```

3. install the dependencies:

    ```bash
    task
    ```

---
