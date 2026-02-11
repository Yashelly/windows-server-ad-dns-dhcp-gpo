# Runbook: Domain join fails

## Symptoms
- Error joining domain (`The specified domain either does not exist...`)
- Credentials rejected, secure channel issues

## Checks
1. DNS:
   - Client DNS must point to DC
   - `nslookup example.local`
2. Connectivity:
   - `ping 10.10.10.10`
3. Time:
   - `w32tm /query /status`
4. Secure channel (if previously joined):
   - `nltest /sc_verify:example.local`
5. DC health:
   - `dcdiag` (server)

## Where to look (logs)
- Client: **Event Viewer** -> **Windows Logs** -> **System** (Netlogon / DNS / Time-Service)
- DC: **Event Viewer** -> **Windows Logs** -> **System** and **Directory Service**

## Fix (safe)
- Fix DNS on client -> retry join
- Sync time:
  - `w32tm /resync`
- Ensure account used has rights

## Validation
- Join succeeds; reboot
- `nltest /dsgetdc:example.local` returns DC

## Rollback
- Remove from domain back to WORKGROUP (lab), reboot
