# Runbook: Access denied (AD groups / NTFS / share / GPO)

## Symptoms
- User cannot access `\\dc01\Finance` (or similar share)
- User can open folder but cannot create/modify files
- Mapped drive is missing / not mapping
- Only one user affected vs multiple users affected

## Checks
1. Scope:
   - One user vs many?
   - One device vs many?
   - One share vs multiple?
2. Identity on client:
   - `whoami`
   - `whoami /groups`
3. DNS / connectivity (domain basics):
   - `nslookup dc01.example.local`
   - `ping 10.10.10.10`
4. Token refresh after group change:
   - Sign out/in, or:
     - `klist purge` (advanced)
     - `gpupdate /force`

## Where to look (logs)
- Client:
  - **Event Viewer** -> **Windows Logs** -> **System** (SMB client / networking)
  - **Event Viewer** -> **Applications and Services Logs** -> **Microsoft** -> **Windows** -> **GroupPolicy** -> **Operational**
- File server (if separate from DC):
  - **Event Viewer** -> **Windows Logs** -> **Security** (audit access if enabled)

## Fix (safe)

### Step 1 — Verify group membership (expected access)
On admin workstation / DC:

```powershell
Import-Module ActiveDirectory
Get-ADPrincipalGroupMembership "jdoe" | Sort Name | Select Name
```

If missing required group:
```powershell
Add-ADGroupMember -Identity "GG-FIN-Share-RW" -Members "jdoe"
```

### Step 2 — Verify share permissions (SMB)
On file server:

```powershell
Get-SmbShare -Name "Finance"
Get-SmbShareAccess -Name "Finance"
```

If needed (example):
```powershell
Grant-SmbShareAccess -Name "Finance" -AccountName "GG-FIN-Share-RW" -AccessRight Change -Force
```

### Step 3 — Verify NTFS permissions (common root cause)
On file server:

```powershell
$Path="D:\Shares\Finance"
(Get-Acl $Path).Access | Format-Table IdentityReference,FileSystemRights,AccessControlType,IsInherited -AutoSize
```

Look for:
- correct group present (e.g., `GG-FIN-Share-RW`)
- broken inheritance / unexpected Deny entries

### Step 4 — Check GPO impact (drive mapping / filtering)
On client:

```cmd
gpresult /r
```
Advanced:
```cmd
gpresult /h %TEMP%\gp.html
```

Common causes:
- wrong OU placement (user/computer)
- security filtering excludes user/group
- DNS issues prevent SYSVOL access (`\\dc01\SYSVOL`)

### Step 5 — Clear cached SMB sessions / credentials
On client:

```cmd
net use
net use \\dc01\Finance /delete
cmdkey /list
```

## Validation
- User can access share and perform required actions (read/write as expected)
- `gpupdate /force` succeeds; `gpresult` shows expected policies
- If group membership was changed, confirm after sign out/in the user token includes new group

## Rollback
- Undo share permission change:
```powershell
Revoke-SmbShareAccess -Name "Finance" -AccountName "GG-FIN-Share-RW" -Force
```
- Undo NTFS ACL change (restore from documented previous ACL / backup)
- Remove incorrect group membership:
```powershell
Remove-ADGroupMember -Identity "GG-FIN-Share-RW" -Members "jdoe" -Confirm:$false
```
