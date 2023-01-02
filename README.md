
# Ansible Role:  `libvirt`

This role configures a host as a [Libvirt/KVM](https://libvirt.org) hypervisor.

It can also configure storage pools and networks on the host.

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-libvirt/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-libvirt)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-libvirt)][releases]
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50067?label=role%20quality)][quality]

[ci]: https://github.com/bodsch/ansible-libvirt/actions
[issues]: https://github.com/bodsch/ansible-libvirt/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-libvirt/releases
[quality]: https://galaxy.ansible.com/bodsch/libvirt


## Supported (tested) Operating systems

Tested on

* Arch Linux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.10


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-libvirt/tags)!


## Configuration

```yaml
libvirt_libvirtd: {}

libvirt_qemu: {}

libvirt_virtual_networks: []

libvirt_storage_pools: []
```

### `libvirt_libvirtd`

```yaml
libvirt_libvirtd:
  # - network
  enable_tls: false
  enable_tcp: false
  tls_port: 16514
  tcp_port: 16509
  listen_addr: "127.0.0.1"
  enable_mdns: false
  # - socket
  unix_sock_group: "libvirt"
  unix_sock_ro_perms: ""  # 0777
  unix_sock_rw_perms: ""  # 0770
  unix_sock_admin_perms: ""  # 0770
  unix_sock_dir: "/run/libvirt"
  # - authentication
  #   - none
  #   - sasl
  #   - polkit
  auth_unix_ro: ""
  auth_unix_rw: ""
  # auth_tcp = "sasl"
  # auth_tls = "none"
  # tcp_min_ssf = 112
  # access_drivers = [ "polkit" ]
  # - TLS x509 certificate configuration
  # key_file = "/etc/pki/libvirt/private/serverkey.pem"
  # cert_file = "/etc/pki/libvirt/servercert.pem"
  # ca_file = "/etc/pki/CA/cacert.pem"
  # crl_file = "/etc/pki/CA/crl.pem"
  # - Authorization controls
  # tls_no_sanity_certificate = 1
  # tls_no_verify_certificate = 1
  # tls_allowed_dn_list = ["DN1", "DN2"]
  # tls_priority="NORMAL"
  # sasl_allowed_username_list = ["joe@EXAMPLE.COM", "fred@EXAMPLE.COM" ]
  # - Processing controls
  max_clients: 5000              # 5000
  max_queued_clients: 1000       # 1000
  max_anonymous_clients: 20      # 20
  min_workers: 5                 # 5
  max_workers: 20                # 20
  prio_workers: 5                # 5
  max_requests: ""               # ?
  max_client_requests: 5         # 5
  admin_min_workers: 1           # 1
  admin_max_workers: 5           # 5
  admin_max_clients: 5           # 5
  admin_max_queued_clients: 5    # 5
  admin_max_client_requests: 5   # 5
  # - Logging controls
  #    1: DEBUG
  #    2: INFO
  #    3: WARNING
  #    4: ERROR
  log_level: 3
  log_filters: []
  #   - 3:remote
  #   - 4:event
  #   - 4:json
  # ="1:qemu 1:libvirt 4:object 4:json 4:event 1:util"
  # Logging outputs:
  # An output is one of the places to save logging information
  # The format for an output can be:
  #    level:stderr
  #      output goes to stderr
  #    level:syslog:name
  #      use syslog for the output and use the given name as the ident
  #    level:file:file_path
  #      output to a file, with the given filepath
  #    level:journald
  #      output to journald logging system
  # In all cases 'level' is the minimal priority, acting as a filter
  #    1: DEBUG
  #    2: INFO
  #    3: WARNING
  #    4: ERROR
  log_outputs: []
  #   - "3:syslog:libvirtd"
  #   - "4:livirtd.log:/var/log/libvirt"
  #   - "3:syslog:libvirtd"
  # - auditing                    #
  #   audit_level == 0  -> disable all auditing
  #   audit_level == 1  -> enable auditing, only if enabled on host (default)
  #   audit_level == 2  -> enable auditing, and exit if disabled on host
  #
  audit_level: 1
  #
  # If set to 1, then audit messages will also be sent
  # via libvirt logging infrastructure. Defaults to 0
  #
  audit_logging: false
  # - UUID of the host
  # host_uuid = "00000000-0000-0000-0000-000000000000"
  # host_uuid_source = "smbios"
  # - Keepalive protocol          #
  keepalive_interval: ""          # 5
  keepalive_count: ""             # 5
  admin_keepalive_interval: ""    # 5
  admin_keepalive_count: ""       # 5
  # - Open vSwitch
  ovs_timeout: ""                 # 5
```

### `libvirt_qemu`

The default security driver is SELinux.
If SELinux is disabled on the host, then the security driver will automatically disable itself.
If you wish to disable QEMU SELinux security driver while leaving SELinux enabled for the host in general,
then set this to `none` instead.
It's also possible to use more than one security driver at the same time, for this use a list of names:

```yaml
  security_driver:
    - selinux
    - apparmor
```

Notes: The DAC security driver is always enabled; as a result, the value of `security_driver` cannot
contain "dac".
The value `none` is a special value; security_driver can be set to that value in isolation, but it cannot appear in a list of drivers.

```yaml
libvirt_qemu:
  security_drivers:
    - apparmor
```

### `libvirt_virtual_networks`

`libvirt_virtual_networks` is a list of networks to define and start.

```yaml
libvirt_virtual_networks:
  - name: ovs-network
    mode: bridge
    bridge_name: br0
    autostart: true
    # active, inactive, present and absent
    state: active
```

### `libvirt_storage_pools`

`libvirt_storage_pools` is a list of storage pools to define and start.

generate a simple used XML file unter `/etc/libvirt/storage`.

[upstream doku](https://libvirt.org/formatstorage.html)

```yaml
libvirt_storage_pools:
  - name: filesystems
    path: /var/lib/libvirt/filesystems/
    autostart: true
    state: active
  - name: lxc
    path: /var/lib/libvirt/lxc
    autostart: true
    state: active
```

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

`FREE SOFTWARE, HELL YEAH!`

