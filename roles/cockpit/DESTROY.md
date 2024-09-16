# Destroy Cockpit

This playbook will remove the Cockpit package from the system.

```yaml
---
- name: Remove cockpit
  hosts: all
  tasks:
    - name: Remove cockpit
      become: true
      ansible.builtin.package:
        name: cockpit
        state: absent

    - name: Delete certificates
      become: true
      ansible.builtin.file:
        path: "{{ item }}"
        state: absent
      with_items:
        - "{{ cockpit_cert_dir | default('/etc/cockpit/ws-certs.d') }}/cert.key"
        - "{{ cockpit_cert_dir | default('/etc/cockpit/ws-certs.d') }}/cert.crt"
```

---
