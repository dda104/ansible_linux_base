import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_cockpit_package_is_installed(host):
    package = host.package("cockpit")
    assert package.is_installed

def test_cockpit_service_is_enabled_running(host):
    service = host.service("cockpit")
    assert service.is_enabled
    assert service.is_running
