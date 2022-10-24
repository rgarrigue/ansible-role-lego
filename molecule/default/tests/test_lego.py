import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "name",
    ["tar"],
)
def test_packages(host, name):
    item = host.package(name)
    assert item.is_installed


@pytest.mark.parametrize(
    "path",
    [
        "/etc/letsencrypt/accounts",
        "/etc/letsencrypt/certificates",
        "/etc/letsencrypt/renew-hooks",
        "/etc/letsencrypt/run-hooks",
        "/usr/bin/lego",
    ],
)
def test_files(host, path):
    with host.sudo():
        item = host.file(path)
        assert item.exists
        assert item.user == "root"
        assert item.group == "root"


def test_command(host):
    with host.sudo():
        cmd = host.check_output("lego --version")
        assert "linux/amd64" in cmd, cmd
