# nmcli

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [nmcli_conn_name](#nmcli_conn_name)
  - [nmcli_dns4](#nmcli_dns4)
  - [nmcli_gw4](#nmcli_gw4)
  - [nmcli_ifname](#nmcli_ifname)
  - [nmcli_restart_network_manager](#nmcli_restart_network_manager)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

None.

## Default Variables

### nmcli_conn_name

#### Default value

```YAML
nmcli_conn_name: '{{ ansible_default_ipv4.interface }}'
```

### nmcli_dns4

#### Default value

```YAML
nmcli_dns4: '{{ nmcli_gw4 }}'
```

### nmcli_gw4

#### Default value

```YAML
nmcli_gw4: 192.168.0.1
```

### nmcli_ifname

#### Default value

```YAML
nmcli_ifname: '{{ ansible_default_ipv4.interface }}'
```

### nmcli_restart_network_manager

#### Default value

```YAML
nmcli_restart_network_manager: true
```

## Dependencies

None.
