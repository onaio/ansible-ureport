import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

UREPORT_VERSION = os.environ['UREPORT_VERSION']


def test_ureport_services(host):
    ureport = host.service("ureport")
    assert ureport.is_running
    assert ureport.is_enabled

    celeryd = host.service("celeryd-ureport")
    assert celeryd.is_running
    assert celeryd.is_enabled

    celery_beat = host.service("celerybeat-ureport")
    assert celery_beat.is_running
    assert celery_beat.is_enabled


def test_ureport_app_files(host):
    app_dir = host.file("/home/ureport/app")
    assert app_dir.exists
    assert app_dir.user == "ureport"
    assert app_dir.group == "www-data"
    assert app_dir.is_symlink
    assert app_dir.linked_to == \
        f"/home/ureport/app-versioned/{UREPORT_VERSION}"

    app_versioned_dir = host.file(
        f"/home/ureport/app-versioned/{UREPORT_VERSION}")
    assert app_versioned_dir.exists
    assert app_versioned_dir.user == "ureport"
    assert app_versioned_dir.group == "www-data"
    assert app_versioned_dir.is_directory
    assert oct(app_versioned_dir.mode) == "0o755"

    virtualenv = host.file("/home/ureport/.virtualenvs/ureport")
    assert virtualenv.exists
    assert virtualenv.user == "ureport"
    assert virtualenv.group == "www-data"
    assert virtualenv.is_directory
    assert oct(virtualenv.mode) == "0o755"


def test_ureport_service_is_up(host):
    sock = host.socket("unix:///var/run/ureport/ureport.sock")
    assert sock.is_listening
