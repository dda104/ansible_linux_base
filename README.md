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

Install rolecule

```shell
sudo dnf install https://github.com/z0mbix/rolecule/releases/download/v0.4.0/rolecule_0.
4.0_linux_amd64.rpm -y
```
