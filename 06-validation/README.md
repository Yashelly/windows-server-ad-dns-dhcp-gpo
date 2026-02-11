# Validation

## Goal
Confirm end-to-end functionality:
- Client `CL01` is domain-joined and uses `DC01` as logon server
- DHCP issues a lease and points DNS to the domain controller
- DNS resolution works for domain hostnames
- Pilot GPO is applied and enforces the intended restriction

## Evidence
- Domain logon proof -> `EVD-VAL-002_cl01-domain-logon.png`
- Group Policy application (`gpresult`) -> `EVD-VAL-001_gpresult-user.png`
- Control Panel blocked -> `EVD-VAL-003_controlpanel-blocked.png`
- DHCP on client (`ipconfig /all`) -> `EVD-LAB-002_ipconfig-cl01.png`
- DNS resolution (`nslookup`) -> `EVD-DNS-002_nslookup-dc01.png`

## Commands used (lab)
- `whoami`
- `echo %logonserver%`
- `gpresult /r`
- `ipconfig /all`
- `nslookup dc01.example.local`

## Planned exports (sanitized)
- `gpresult /h` -> publish to `99-evidence/exports/`
- `dcdiag` -> publish to `99-evidence/exports/`
