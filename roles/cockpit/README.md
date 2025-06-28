# cockpit

Role for configure cockpit

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [cockpit_motd_absent](#cockpit_motd_absent)
  - [cockpit_package_present](#cockpit_package_present)
  - [cockpit_service_enabled](#cockpit_service_enabled)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.11`

## Default Variables

### cockpit_motd_absent

#### Default value

```YAML
cockpit_motd_absent: false
```

### cockpit_package_present

#### Default value

```YAML
cockpit_package_present: true
```

### cockpit_service_enabled

#### Default value

```YAML
cockpit_service_enabled: true
```

## Dependencies

- dda104.linux_base.packages

## License

Unlicense

## Author

Denis Dvornikov
