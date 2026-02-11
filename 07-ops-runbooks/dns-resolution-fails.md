# Runbook: DNS resolution fails

## Symptoms
- Client cannot resolve `dc01.example.local` or `example.local`
- Domain logon issues, GPO not applying

## Checks
1. On client:
   - `ipconfig /all` -> verify DNS server points to DC
   - `nslookup dc01.example.local`
2. On server:
   - **DNS Manager** -> confirm `example.local` zone exists
   - Check `dc01` A record exists (Forward Lookup Zone)
   - Event logs (server): **Event Viewer** -> **Applications and Services Logs** -> **DNS Server**
3. Network:
   - `ping 10.10.10.10` (DC IP)

## Where to look (logs)
- Client: **Event Viewer** -> **Applications and Services Logs** -> **Microsoft** -> **Windows** -> **DNS Client Events** -> **Operational**
- Server: **Event Viewer** -> **Applications and Services Logs** -> **DNS Server**

## Fix (safe)
- Set client DNS to DC IP
- Restart DNS service (only if needed):
  - `Restart-Service DNS`
- Re-register DNS:
  - `ipconfig /registerdns`

## Validation
- `Resolve-DnsName dc01.example.local`
- Domain login works; `gpupdate /force` succeeds

## Rollback
- Undo DNS change on client (back to DHCP option)
