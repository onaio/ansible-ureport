onaio - U-Report [![Build Status](https://github.com/onaio/ansible-ureport/workflows/CI/badge.svg)](https://github.com/onaio/ansible-ureport/actions?query=workflow%3ACI)
=========

Installs and configures [U-Report](https://github.com/rapidpro/ureport/)

Requirements
------------

U-Report has the following requirements:

- PostgreSQL
- Redis

Role Variables
--------------

Check the [defaults/main.yml](./defaults/main.yml) file for the full list of default variables.

Dependencies
------------

Here's the list of role dependencies:

- [onaio.django](https://github.com/onaio/ansible-django)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yml
---
- hosts: all
  roles:
    - role: onaio.postgresql
      vars:
        postgresql_version: 10
        postgresql_users:
          - name: ureport
            pass: ureport
            encrypted: true
        postgresql_databases:
          - name: ureport
            owner: ureport
            encoding: UTF-8
            hstore: true
        postgresql_database_extensions:
          - db: ureport
            extensions:
              - hstore
        postgresql_backup_enabled: false

    - role: DavidWittman.redis
      vars:
        redis_version: "2.8.24"

    - role: ansible-ureport
      vars:
        ureport_postgresql_password: ureport
```

License
-------

Apache 2
