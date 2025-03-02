# Collection dda104.linux_base

## Prepare

Install tools via [asdf](https://asdf-vm.com):

```shell
cat .tool-versions | awk '{print $1}' | xargs -i asdf plugin add {}
asdf install
```

Prepare direnv:

```shell
# direnv hook $SHELL >> ~/.<shellrc>
direnv hook $SHELL >> ~/.bashrc

direnv allow
```

Install dependencies:

```shell
task
```
