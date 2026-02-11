# STATUS

Evidence maturity:
- **Captured** -> sanitized evidence exists in `99-evidence/`
- **Partial** -> implemented but evidence is incomplete
- **Planned** -> not implemented or not captured yet

## A) Lab environment
- **A1 (Captured)** -> Lab subnet `10.10.10.0/24` + DC01 static IP -> `EVD-LAB-001_ipconfig-dc01.png`
- **A2 (Captured)** -> Client CL01 obtains DHCP lease + DNS from DC01 -> `EVD-LAB-002_ipconfig-cl01.png`

## B) AD DS (Domain Controller)
- **B1 (Captured)** -> AD DS role install -> `EVD-AD-001_adds-role.png`
- **B2 (Captured)** -> Domain visible in ADUC (post-promo) -> `EVD-AD-002_domain-visible-aduc.png`
- **B3 (Captured)** -> Server Manager roles after promotion -> `EVD-AD-004_servermanager-after-promo.png`
- **B4 (Captured)** -> Prerequisites check warning (DNS delegation note) -> `EVD-AD-003_prereq-dns-delegation.png`

## C) DNS
- **C1 (Captured)** -> Forward lookup zone + host records -> `EVD-DNS-001_forward-zone-example-local.png`
- **C2 (Captured)** -> Name resolution validation (`nslookup`) -> `EVD-DNS-002_nslookup-dc01.png`
- **C3 (Planned)** -> Reverse lookup zone + PTR validation (if implemented, capture DNS Manager view)

## D) DHCP
- **D1 (Captured)** -> DHCP scope created -> `EVD-DHCP-001_scope.png`
- **D2 (Captured)** -> Active lease observed for CL01 -> `EVD-DHCP-002_address-leases.png`
- **D3 (Planned)** -> Scope options (DNS server, default gateway) evidence (capture `Scope Options`)
- **D4 (Planned)** -> Reservation example (optional)

## E) Group Policy
- **E1 (Captured)** -> GPO linked to pilot OU (`PilotUsers`) -> `EVD-GPO-001_linked-gpo-to-ou-pilotusers.png`
- **E2 (Captured)** -> Policy enabled (Control Panel restriction) -> `EVD-GPO-002_prohibit-controlpanel-enabled.png`

## F) Validation
- **F1 (Captured)** -> Domain logon proof (`whoami` + `%logonserver%`) -> `EVD-VAL-002_cl01-domain-logon.png`
- **F2 (Captured)** -> Policy applied (`gpresult`) -> `EVD-VAL-001_gpresult-user.png`
- **F3 (Captured)** -> Control Panel blocked on client -> `EVD-VAL-003_controlpanel-blocked.png`

## G) Ops runbooks
- **G1 (DOC-ONLY)** -> Runbooks present under `07-ops-runbooks/`

## H) Expansion modules
- **H1 (Planned)** -> File services module (SMB + NTFS) evidence capture -> `08-file-services/`
- **H2 (Planned)** -> Backup/recovery module evidence capture -> `09-backup-recovery/`

## Backlog
- **Exports pack (Planned)** -> `dcdiag`, `repadmin /replsummary`, `gpresult /h`, `ipconfig /all` -> publish sanitized under `99-evidence/exports/`
