import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_firewalld_package_is_installed(host):
    package = host.package("firewalld")
    assert package.is_installed

def test_firewalld_service_is_enabled_running(host):
    service = host.service("firewalld")
    assert service.is_enabled
    assert service.is_running
