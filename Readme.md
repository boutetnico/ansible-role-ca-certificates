[![tests](https://github.com/boutetnico/ansible-role-ca-certificates/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-ca-certificates/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.ca_certificates-blue.svg)](https://galaxy.ansible.com/boutetnico/ca_certificates)

ansible-role-ca-certificates
============================

This role installs and configures ca-certificates.

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

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
