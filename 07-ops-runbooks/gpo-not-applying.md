# Runbook: GPO not applying

## Symptoms
- Policy behavior not present on client
- `gpresult` doesn't list expected GPO

## Checks
1. Client:
   - `gpupdate /force`
   - `gpresult /r`
   - `gpresult /h .\gpresult.html`
   - SYSVOL reachability: open `\\dc01\SYSVOL` (or `\\example.local\SYSVOL`)
2. GPMC:
   - Link is to the correct OU
   - Security filtering / WMI filter not blocking
   - User/computer is in correct OU
3. Network/time:
   - DNS resolution to DC
   - `w32tm /query /status`

## Where to look (logs)
- Client: **Event Viewer** -> **Applications and Services Logs** -> **Microsoft** -> **Windows** -> **GroupPolicy** -> **Operational**
- DC: **Event Viewer** -> **Windows Logs** -> **System** and **Directory Service**

## Fix (safe)
- Move object to correct OU
- Adjust security filtering (apply to test group)
- Remove/disable conflicting WMI filter

## Validation
- `gpupdate /force` succeeds
- `gpresult` shows the GPO

## Rollback
- Unlink GPO / set to **Not Configured**
