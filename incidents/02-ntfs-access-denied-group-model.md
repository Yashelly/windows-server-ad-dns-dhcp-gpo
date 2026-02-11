# Incident record: SMB/NTFS "Access Denied" (group-based permissions)

Evidence:
- screenshot of error
- `whoami /all` (group membership)
- share + NTFS ACL screenshots

Root cause:
- missing required AD group membership or stale token

Remediation:
- Added user to the required AD group (avoid per-user ACL entries)
- User re-logon to refresh token
- Validated access
