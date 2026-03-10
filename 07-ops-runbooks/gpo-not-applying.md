# Runbook: GPO not applying

## Symptoms
- Policy behavior not present on client
- `gpresult` doesn't list expected GPO
- Restrictions / drive mappings do not apply

## Checks
1. Client:
   - `gpupdate /force`
   - `gpresult /r`
   - `gpresult /h %TEMP%\gpresult.html`
   - SYSVOL reachability:
     - `\\dc01\SYSVOL` and/or `\\example.local\SYSVOL`
2. GPMC (on DC01 or admin workstation):
   - GPO is linked to the correct OU
   - Security filtering / WMI filter is not blocking
   - User/computer is in the expected OU
3. Domain basics:
   - Client DNS points to `10.10.10.10`
   - Time is in sync: `w32tm /query /status`

## Where to look (logs)
- Client: **Event Viewer** -> **Applications and Services Logs** -> **Microsoft** -> **Windows** -> **GroupPolicy** -> **Operational**
- DC: **Event Viewer** -> **Windows Logs** -> **System** and **Directory Service**

## Fix (safe)
- Fix DNS first (common root cause in labs).
- Move object to correct OU (user/computer).
- Adjust security filtering (apply to a test group first).
- Remove/disable conflicting WMI filter.

## Validation
- `gpupdate /force` succeeds without errors
- `gpresult /r` shows expected GPO
- `%TEMP%\gpresult.html` opens and confirms expected settings

## Rollback
- Unlink GPO / set settings to **Not Configured**
