import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("ca-certificates"),
    ],
)
def test_dependencies_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "file,user,group,mode",
    [
        ("cert1.pem", "root", "root", 0o644),
    ],
)
def test_certificate_files_exist(host, file, user, group, mode):
    cert = host.file("/usr/share/ca-certificates/" + file)
    assert cert.exists
    assert cert.is_file
    assert cert.user == user
    assert cert.group == group
    assert cert.mode == mode


def test_ca_certificates_command_works(host):
    cmd = host.run("update-ca-certificates --help")
    assert cmd.rc == 0


def test_ca_certificates_directory_exists(host):
    directory = host.file("/usr/share/ca-certificates")
    assert directory.exists
    assert directory.is_directory
