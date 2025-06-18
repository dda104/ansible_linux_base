# Collection dda104.linux_base

## Usage

Create requirements.yml:

```yaml
---
collections:
  - name: dda104.linux_base
    source: https://gitlab.com/ansible_public/dda104.linux_base
    type: git
    version: 1.2.1
```

Install collection via uv:

```shell
uv run ansible-galaxy install -r requirements.yml
```

## Development

### Prepare

Install tools via [asdf](https://asdf-vm.com) and uv:

```shell
cat .tool-versions | awk '{print $1}' | xargs -i asdf plugin add {}
asdf install
uv sync
```
