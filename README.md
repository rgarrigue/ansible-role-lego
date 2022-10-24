# Ansible role lego

Setup Lego, an alternative to certbot to provides certificates through the ACME protocol, and specificaly let's encrypt in our case.

Note, there are two directories meant for hooks where you can drop scripts that'll be executed via run-parts (hence chmod +x, shebang and no .sh or whatever extension):

- `/etc/letsencrypt/run-hooks` will be executed on every Ansible run. That's meant for initial certificates generation, but happens everytime.
- `/etc/letsencrypt/renew-hooks` will be executed by the daily "certificate renewal" cron.

This role is tested using [Molecule](https://molecule.readthedocs.io/). The default will use Docker that you must install yourself. Then run `tox` to setup python environment and start testing. If docker can't do, podman is a possibility running `tox -- test -d podman`. If neither docker or podman can do, for example if the role contains containers related tasks, Vagrant & KVM via libvirt is also possible, running `tox -- test -s vagrant`.

A [Vagrantfile](https://www.vagrantup.com/) is also provided for development purpose. Install Vagrant and VirtualBox (or libvirt / KVM), then run `vagrant up`.

## Requirements

Python & [tox](https://tox.readthedocs.io). See imports in `library/*` and tasks in `molecule/default/converge.yml` if any specific, but those should be added in `tox.ini`.

## Role Variables

See [defaults/main.yml](defaults/main.yml).

## Dependencies

See [meta/main.yml](meta/main.yml) and [molecule/default/requirements.yml](molecule/default/requirements.yml) if any.

## Example Playbook

```yaml
- hosts: all
  roles:
    - lego
```

## License

MIT

## Author Information
