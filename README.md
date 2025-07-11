# Collection dda104.linux_base

TODO: fix gather var in nmcli role argument specs

## Usage

Create requirements.yml:

```yaml
---
collections:
  - name: dda104.linux_base
    source: git@gitlab.com:dda104/linux_base.git
    type: git
    version: 1.10.0
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
