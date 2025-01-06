# firewalld

Role for configure firewalld

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [firewalld_enabled](#firewalld_enabled)
  - [firewalld_ports_list](#firewalld_ports_list)
  - [firewalld_reboot_machine](#firewalld_reboot_machine)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.11`

## Default Variables

### firewalld_enabled

#### Default value

```YAML
firewalld_enabled: false
```

### firewalld_ports_list

#### Default value

```YAML
firewalld_ports_list: []
```

### firewalld_reboot_machine

#### Default value

```YAML
firewalld_reboot_machine: true
```



## Dependencies

None.

## License

Unlicense

## Author

Denis Dvornikov
