# 09-backup-recovery (basic)

## Goal
Capture a simple, realistic backup/recovery story for a lab:
- What is backed up (system state / VM snapshots / configs)
- Restore point strategy
- Validation after restore (AD DS health, DNS/DHCP service status)

Approach: snapshots before risky changes; restore to prove rollback.

## Evidence checklist (suggested)
- [ ] Hypervisor snapshot list (sanitized)
- [ ] Restore action screenshot/log (sanitized)
- [ ] Post-restore checks: `dcdiag`, `nslookup`, DHCP lease test

## Captured evidence

- _No captured evidence committed yet for this module._

