# ROADMAP

## v0.1.1 (current publish)
- Core lab documented and validated: AD DS + DNS + DHCP + pilot GPO + domain join
- Sanitized evidence pack in `99-evidence/screenshots/` with an index (`99-evidence/EVIDENCE-MAP.md`)
- Ops runbooks for common issues (DNS/DHCP/GPO/domain join)
- Overview/meta-doc refactor aligned to the portfolio module structure
- Expansion module stubs present (docs-only): `08-file-services/`, `09-backup-recovery/`

## v0.2.0 (diagnostics + DNS/DHCP refinements)
- Publish `dcdiag` output (sanitized)
- Add DHCP options export / screenshot evidence
- Add DNS reverse zone / PTR validation
- Add one DHCP reservation example

## v0.3.0 (access + recovery)
- File services implementation with SMB share + NTFS model
- Captured “access denied” evidence tied to a lab-consistent scenario
- Snapshot/recovery walkthrough with before/after validation

## v0.4.0 (hardening + automation)
- Additional computer-side GPO baseline
- Small PowerShell validation helpers
- Evidence quality gate improvements in CI / repo checks