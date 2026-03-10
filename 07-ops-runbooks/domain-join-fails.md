# Runbook: Domain join fails

## Symptoms
- Error joining domain (`The specified domain either does not exist...`)
- Credentials rejected
- Secure channel issues (re-join scenarios)

## Checks
1. DNS (most common):
   - Client DNS must point to `10.10.10.10`
   - Client DNS suffix should be `example.local` (often from DHCP option 015)
   - `nslookup example.local`
   - `nslookup dc01.example.local`
2. Connectivity:
   - `ping 10.10.10.10`
3. Time (Kerberos):
   - `w32tm /query /status`
4. Domain controller discovery (even before join you can test DNS; after join this must work):
   - `nltest /dsgetdc:example.local`
5. DC health (on DC01):
   - `dcdiag`

## Where to look (logs)
- Client: **Event Viewer** -> **Windows Logs** -> **System** (Netlogon / DNS / Time-Service)
- DC: **Event Viewer** -> **Windows Logs** -> **System** and **Directory Service**

## Fix (safe)
1. Fix DNS on client -> retry join
2. Sync time:
   - `w32tm /resync`
3. Use correct credential format when joining:
   - `EXAMPLE\Administrator` or `Administrator@example.local`
4. If the computer account exists but is broken:
   - Remove/reset the computer account in AD (lab) and re-join

## Validation
- Join succeeds; reboot
- Domain discovery returns DC01:
  - `nltest /dsgetdc:example.local` -> `\\DC01.example.local (10.10.10.10)`

## Rollback
- Remove from domain back to WORKGROUP (lab), reboot
