# Runbook: DHCP client gets no lease

## Symptoms
- `ipconfig /all` shows APIPA (169.254.x.x)
- No DNS suffix / DNS server
- Client cannot reach `10.10.10.10`

## Checks
1. Client:
   - `ipconfig /release` -> `ipconfig /renew`
   - Check link status (NIC enabled, connected)
2. Server (DC01):
   - **DHCP Manager** -> scope is **Active**
   - Address pool not exhausted (expected range: `10.10.10.50` – `10.10.10.200`)
   - Leases view -> confirm client MAC is receiving a lease
   - Service status: `Get-Service DHCPServer`
   - Scope list: `Get-DhcpServerv4Scope`
   - Options: `Get-DhcpServerv4OptionValue -ScopeId 10.10.10.0`
3. Network:
   - DHCP relay? (usually none in a single-subnet lab)

## Where to look (logs)
- Client: **Event Viewer** -> **Windows Logs** -> **System** (source: **Dhcp-Client**)
- Server: **Event Viewer** -> **Applications and Services Logs** -> **Microsoft** -> **Windows** -> **DHCP-Server** -> **Operational**

## Fix (safe)
1. Activate scope (if inactive).
2. Confirm options on the scope (lab expected values):
   ```powershell
   Get-DhcpServerv4OptionValue -ScopeId 10.10.10.0 | Select OptionId, Name, Value
   ```
   - 006 DNS Servers: `10.10.10.10`
   - 015 DNS Domain Name: `example.local`
   - 003 Router: *(blank in this lab; no default gateway)*
3. Restart DHCP service **only if needed**:
   - `Restart-Service DHCPServer`

## Validation
- Client gets IP from scope: `10.10.10.50` – `10.10.10.200` (example confirmed: `10.10.10.50`)
- `ipconfig /all` shows:
  - DNS suffix: `example.local`
  - DHCP server: `10.10.10.10`
  - DNS server: `10.10.10.10`
  - Default gateway: *(blank in this lab)*
- Client can resolve DC:
  - `nslookup dc01.example.local` -> `10.10.10.10`

## Rollback
- Revert scope changes / options to previous values
