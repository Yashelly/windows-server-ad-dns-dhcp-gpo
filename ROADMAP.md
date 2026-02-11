# ROADMAP

## v0.1.0 (initial publish)
- Core lab documented and validated: AD DS + DNS + DHCP + pilot GPO + domain join
- Sanitized evidence pack in `99-evidence/screenshots/` with an index (`99-evidence/EVIDENCE-MAP.md`)
- Ops runbooks for common issues (DNS/DHCP/GPO/domain join)
- Expansion module stubs present (docs-only): `08-file-services/`, `09-backup-recovery/`

## v0.2.0 (diagnostics + DNS/DHCP refinements)
- Publish a small diagnostics export pack under `99-evidence/exports/` (sanitized):
  - `dcdiag`
  - `repadmin /replsummary`
  - `gpresult /h`
  - `ipconfig /all` (text export versions; screenshots already exist)
- DNS: reverse lookup zone + PTR validation (if implemented)
- DHCP: capture scope options (DNS server, router) evidence

## v0.3.0 (hardening expansion)
- Baseline GPO set (password policy, lock screen, firewall baseline)
- Optional: LAPS notes and implementation approach for the lab
- Backup/recovery implementation + captured evidence for `09-backup-recovery/` (currently docs-only)

## v0.4.0 (file services module)
- SMB share + NTFS group model implementation + evidence for `08-file-services/` (currently docs-only)
- Incident example with evidence (Access Denied -> fix -> validate)
