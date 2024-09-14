import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_vim_package_absent(host):
    vim = host.package("vim")
    assert not vim.is_installed

def test_git_package_present(host):
    git = host.package("git")
    assert git.is_installed
