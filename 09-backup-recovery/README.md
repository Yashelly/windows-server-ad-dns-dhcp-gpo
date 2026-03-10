# 09-backup-recovery (basic)

## Goal

Capture a simple, realistic backup and recovery story for the lab:
- what is backed up (system state / VM snapshots / configs)
- restore point strategy
- validation after restore (AD DS health, DNS/DHCP service status)

## Implementation summary

- This module is documentation-first and describes the intended recovery model for the lab.
- The current approach assumes snapshots before risky changes and validation after restore.
- Captured recovery evidence is planned, not yet published.

## Validation

When implemented, recovery validation should confirm:
- the domain controller boots normally after restore
- AD DS, DNS, and DHCP services start successfully
- client domain logon still works
- DNS and DHCP baseline behavior remains unchanged

Suggested checks:
```powershell
Get-Service NTDS, DNS, DHCPServer
dcdiag
```
Client-side:
```cmd
echo %logonserver%
nslookup dc01.example.local
ipconfig /all
```

## Rollback

If a restore attempt introduces drift:
- revert to the previous known-good snapshot
- compare service state and IP/DNS settings to baseline
- re-run the validation set before marking the lab healthy again

## Evidence

Planned evidence:
- snapshot inventory screenshot
- restore summary note
- post-restore validation output