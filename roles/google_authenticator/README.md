# google_authenticator

Role for configure auth via google_authenticator

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [google_authenticator_additional_ssh_config](#google_authenticator_additional_ssh_config)
  - [google_authenticator_ssh_allow_additional_users](#google_authenticator_ssh_allow_additional_users)
  - [google_authenticator_user](#google_authenticator_user)
  - [google_authenticator_user_home](#google_authenticator_user_home)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.11`

## Default Variables

### google_authenticator_additional_ssh_config

#### Default value

```YAML
google_authenticator_additional_ssh_config:
```

### google_authenticator_ssh_allow_additional_users

#### Default value

```YAML
google_authenticator_ssh_allow_additional_users:
```

### google_authenticator_user

#### Default value

```YAML
google_authenticator_user: user
```

### google_authenticator_user_home

#### Default value

```YAML
google_authenticator_user_home: /home/{{ google_authenticator_user }}
```

## Discovered Tags

**_skip_ansible_lint_**

## Dependencies

- dda104.linux_base.packages

## License

Unlicense

## Author

Denis Dvornikov
