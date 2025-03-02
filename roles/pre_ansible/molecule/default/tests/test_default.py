import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_python3_libdnf5_package_present(host):
    python3_libdnf5 = host.package("python3-libdnf5")
    assert python3_libdnf5.is_installed

def test_python3_rpm_package_present(host):
    python3_rpm = host.package("python3-libdnf5")
    assert python3_rpm.is_installed
