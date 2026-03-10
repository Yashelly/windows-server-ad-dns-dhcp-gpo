# 08-file-services (SMB shares + NTFS)

## Goal
Demonstrate basic file services administration:
- SMB share creation
- NTFS permissions model (group-based access)
- Typical incident: "Access Denied" -> evidence -> fix -> validate

## Implementation summary
- This module is documentation-first and is not yet backed by captured evidence from the current lab.
- The intended scenario uses group-based share and NTFS permissions, with troubleshooting artifacts documented as synthetic examples.
- Related examples are intentionally separated from the core validated lab scope.

## Validation
When implemented, validation should confirm:
- the share is reachable from a domain-joined client
- read/write behavior matches group membership
- share permissions and NTFS ACLs are aligned
- an "access denied" case can be reproduced and resolved cleanly

Suggested checks:
```powershell
Get-SmbShare
Get-SmbShareAccess -Name "Finance"
(Get-Acl "D:\Shares\Finance").Access
```

## Rollback
Safe rollback options:
- remove the test share
- restore the previous NTFS ACL
- remove the test group membership used for validation

## Evidence
Planned evidence:
- share properties screenshot
- NTFS permissions screenshot
- test access screenshot from client
- synthetic incident note:
 - ../ticket-notes/02-ntfs-access-denied.md

## Notes
This module remains outside the fully validated baseline until evidence is captured from the current lab.