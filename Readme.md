[![tests](https://github.com/boutetnico/ansible-role-ca-certificates/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-ca-certificates/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.ca_certificates-blue.svg)](https://galaxy.ansible.com/boutetnico/ca_certificates)

ansible-role-ca-certificates
============================

This role installs and configures ca-certificates.

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                    | Required | Default             | Choices   | Comments                                 |
|-----------------------------|----------|---------------------|-----------|------------------------------------------|
| cacertificates_dependencies | true     | `ca-certificates`   | string    |                                          |
| cacertificates_files        | true     | `[]`                | list      |                                          |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-ca-certificates

          cacertificates_files:
            - src: certs/cert1.pem
              dest: cert1.pem



Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
