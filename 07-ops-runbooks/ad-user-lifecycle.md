# Runbook: AD user lifecycle (create/disable/reset/groups)

## Scope
Lab domain conventions used in this repo (see `../LAB-CONSTANTS.md`):
- Domain: `example.local` (NetBIOS: `EXAMPLE`)
- Domain controller: `dc01.example.local` (`10.10.10.10`)
- Example OU: `OU=Users,OU=Corp,DC=example,DC=local`

## Requests / scenarios
- Create a new user (new starter)
- Disable user (leaver)
- Enable user (rehire)
- Reset password + force change at next logon
- Unlock account
- Add/remove group membership

## Checks (before changes)
1. Confirm you are targeting the correct object:
   - User exists? `Get-ADUser <sam>`
2. Confirm you have the right OU DN:
   - Common failure = typo in DN
3. Confirm AD module is available:
   - `Get-Module -ListAvailable ActiveDirectory`
4. If access is group-based, remember token refresh may be needed after changes.

## Fix (safe)

### A) Create a new user (standard)
PowerShell (run on DC or RSAT machine):

```powershell
Import-Module ActiveDirectory

$GivenName  = "John"
$Surname    = "Doe"
$Display    = "$GivenName $Surname"
$Sam        = "jdoe"
$Upn        = "$Sam@example.local"
$OuDn       = "OU=Users,OU=Corp,DC=example,DC=local"
$TempPwd    = ConvertTo-SecureString "P@ssw0rd-Temp-123!" -AsPlainText -Force

New-ADUser `
  -Name $Display `
  -GivenName $GivenName `
  -Surname $Surname `
  -DisplayName $Display `
  -SamAccountName $Sam `
  -UserPrincipalName $Upn `
  -Path $OuDn `
  -AccountPassword $TempPwd `
  -Enabled $true `
  -ChangePasswordAtLogon $true `
  -PasswordNeverExpires $false
```

Optional: add to a role group (recommended over per-user permissions):
```powershell
Add-ADGroupMember -Identity "GG-FIN-Users" -Members "jdoe"
```

### B) Disable a user (leaver)
```powershell
Disable-ADAccount -Identity "jdoe"
```

Optional hardening (use case-dependent):
- Remove from non-default groups
- Reset password (invalidate cached credentials)
- Move to a “Disabled Users” OU

```powershell
# list groups
Get-ADPrincipalGroupMembership "jdoe" | Select Name

# remove from a specific group
Remove-ADGroupMember -Identity "GG-FIN-Users" -Members "jdoe" -Confirm:$false

# move to disabled OU (example)
Move-ADObject -Identity (Get-ADUser "jdoe").DistinguishedName -TargetPath "OU=Disabled,OU=Corp,DC=example,DC=local"
```

### C) Enable a user
```powershell
Enable-ADAccount -Identity "jdoe"
```

### D) Reset password + force change
```powershell
$NewPwd = ConvertTo-SecureString "N3wTempPwd-123!" -AsPlainText -Force
Set-ADAccountPassword -Identity "jdoe" -Reset -NewPassword $NewPwd
Set-ADUser -Identity "jdoe" -ChangePasswordAtLogon $true
```

### E) Unlock account
```powershell
Unlock-ADAccount -Identity "jdoe"
```

### F) Add/remove group membership
Add:
```powershell
Add-ADGroupMember -Identity "GG-FIN-Users" -Members "jdoe"
```
Remove:
```powershell
Remove-ADGroupMember -Identity "GG-FIN-Users" -Members "jdoe" -Confirm:$false
```

## Where to look (logs) (optional)
If auditing is enabled, events may appear in:
- DC: **Event Viewer** -> **Windows Logs** -> **Security**
  - User created: 4720
  - User disabled/enabled: 4725 / 4722
  - Password reset: 4724
  - Account locked/unlocked: 4740 / 4767

## Validation
- Verify object state:
```powershell
Get-ADUser "jdoe" -Properties Enabled,LockedOut,PasswordLastSet,LastLogonDate,DistinguishedName |
  Select SamAccountName,Enabled,LockedOut,PasswordLastSet,LastLogonDate,DistinguishedName
```
- Verify group membership:
```powershell
Get-ADPrincipalGroupMembership "jdoe" | Sort Name | Select Name
```

## Rollback
- If user created incorrectly:
  - Disable the account first, then delete if required:
```powershell
Disable-ADAccount "jdoe"
Remove-ADUser "jdoe" -Confirm:$true
```
- If group membership added incorrectly:
```powershell
Remove-ADGroupMember "GG-FIN-Users" "jdoe" -Confirm:$false
```
