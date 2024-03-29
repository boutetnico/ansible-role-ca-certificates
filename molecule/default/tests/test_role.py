import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("ca-certificates"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "file,user,group,mode",
    [
        ("cert1.pem", "root", "root", 0o644),
    ],
)
def test_certificate_files_exist(host, file, user, group, mode):
    config = host.file("/usr/share/ca-certificates/" + file)
    assert config.exists
    assert config.is_file
    assert config.user == user
    assert config.group == group
    assert config.mode == mode
