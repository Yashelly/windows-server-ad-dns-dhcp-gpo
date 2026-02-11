# EVIDENCE MAP

Location:
- Screenshots -> `99-evidence/screenshots/`
- Exports/logs (sanitized) -> `99-evidence/exports/`, `99-evidence/logs/`

## AD DS
- `EVD-AD-001_adds-role.png` -> AD DS role install progress/results
- `EVD-AD-002_domain-visible-aduc.png` -> Domain tree + OU visible in **Active Directory Users and Computers**
- `EVD-AD-003_prereq-dns-delegation.png` -> Prerequisites check (DNS delegation note)
- `EVD-AD-004_servermanager-after-promo.png` -> Server Manager roles after promotion

## DNS
- `EVD-DNS-001_forward-zone-example-local.png` -> Forward lookup zone view (`example.local`)
- `EVD-DNS-002_nslookup-dc01.png` -> `nslookup` validation for `dc01.example.local`

## DHCP
- `EVD-DHCP-001_scope.png` -> DHCP scope (`10.10.10.0/24`)
- `EVD-DHCP-002_address-leases.png` -> Active address lease for client

## GPO
- `EVD-GPO-001_linked-gpo-to-ou-pilotusers.png` -> GPO linked to pilot OU
- `EVD-GPO-002_prohibit-controlpanel-enabled.png` -> Policy setting enabled (Control Panel restriction)

## Lab network
- `EVD-LAB-001_ipconfig-dc01.png` -> DC01 network settings (static IP)
- `EVD-LAB-002_ipconfig-cl01.png` -> CL01 network settings (DHCP + DNS)

## Validation
- `EVD-VAL-001_gpresult-user.png` -> `gpresult` confirms applied GPO(s)
- `EVD-VAL-002_cl01-domain-logon.png` -> `whoami` + `%logonserver%` proof
- `EVD-VAL-003_controlpanel-blocked.png` -> Client restriction dialog
