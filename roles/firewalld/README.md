# firewalld

Role for configure firewalld

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [firewalld_enabled](#firewalld_enabled)
  - [firewalld_reboot_machine](#firewalld_reboot_machine)
  - [firewalld_reload](#firewalld_reload)
  - [firewalld_reload_zones](#firewalld_reload_zones)
  - [firewalld_zones](#firewalld_zones)
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
firewalld_enabled: true
```

### firewalld_reboot_machine

#### Default value

```YAML
firewalld_reboot_machine: false
```

### firewalld_reload

#### Default value

```YAML
firewalld_reload: false
```

### firewalld_reload_zones

#### Default value

```YAML
firewalld_reload_zones: false
```

### firewalld_zones

#### Default value

```YAML
firewalld_zones: []
```

## Dependencies

- dda104.linux_base.packages

## License

Unlicense

## Author

Denis Dvornikov
