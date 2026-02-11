# Runbook: DHCP client gets no lease

## Symptoms
- `ipconfig /all` shows APIPA (169.254.x.x)
- No default gateway / DNS

## Checks
1. Client:
   - `ipconfig /release` -> `ipconfig /renew`
2. Server:
   - **DHCP Manager** -> scope is **Active**
   - Address pool not exhausted
   - Leases view
   - Service status: `Get-Service DHCPServer`
   - Event logs (server): **Event Viewer** -> **Applications and Services Logs** -> **Microsoft** -> **Windows** -> **DHCP-Server** -> **Operational**
3. Network:
   - DHCP relay? (usually none in single-subnet lab)

## Where to look (logs)
- Client: **Event Viewer** -> **Windows Logs** -> **System** (source: **Dhcp-Client**)
- Server: **Event Viewer** -> **Applications and Services Logs** -> **Microsoft** -> **Windows** -> **DHCP-Server** -> **Operational**

## Fix (safe)
- Activate scope
- Confirm options 003/006/015
- Restart DHCP service (only if needed):
  - `Restart-Service DHCPServer`

## Validation
- Client gets IP from scope
- DNS suffix is correct, DNS points to DC

## Rollback
- Revert scope changes / options
