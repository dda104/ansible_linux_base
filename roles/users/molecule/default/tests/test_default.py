import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_user1_exists(host):
    user = host.user("user1")
    assert user.exists

def test_user2_exists(host):
    user = host.user("user2")
    assert user.exists

def test_user2_sudo_file(host):
    f = host.file("/etc/sudoers.d/user2")
    assert f.exists

def test_user3_exists(host):
    user = host.user("user3")
    assert not user.exists

def test_user4_exists(host):
    user = host.user("user4")
    assert user.exists
    assert user.uid == 1999
