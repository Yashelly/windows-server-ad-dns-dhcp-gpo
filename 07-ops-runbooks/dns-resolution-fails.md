# Runbook: DNS resolution fails

## Symptoms
- Client cannot resolve `dc01.example.local` or `example.local`
- Domain logon issues, GPO not applying
- Name resolution works intermittently

## Checks
1. On client (CL01):
   - `ipconfig /all` -> verify:
     - DNS suffix: `example.local`
     - DNS server: `10.10.10.10`
     - DHCP server: `10.10.10.10`
   - `nslookup dc01.example.local`
   - `nslookup example.local`
2. On server (DC01):
   - **DNS Manager** -> confirm `example.local` zone exists
   - Confirm `dc01` A record exists (Forward Lookup Zone)
   - Confirm `_msdcs.example.local` zone exists
3. Connectivity:
   - `ping 10.10.10.10`

## Where to look (logs)
- Client: **Event Viewer** -> **Applications and Services Logs** -> **Microsoft** -> **Windows** -> **DNS Client Events** -> **Operational**
- Server: **Event Viewer** -> **Applications and Services Logs** -> **DNS Server**

## Fix (safe)
1. Ensure client DNS = `10.10.10.10` (preferred for a single-DC lab).
2. Re-register DNS on client:
   - `ipconfig /registerdns`
3. Clear DNS cache on client:
   - `ipconfig /flushdns`
4. Restart DNS service **only if configuration/records are correct and issues persist**:
   - `Restart-Service DNS`

## Validation
- `nslookup dc01.example.local` returns `10.10.10.10`
- `Resolve-DnsName dc01.example.local` succeeds
- `gpupdate /force` succeeds (if domain-joined)

## Rollback
- Undo client DNS change (back to DHCP option 006)
