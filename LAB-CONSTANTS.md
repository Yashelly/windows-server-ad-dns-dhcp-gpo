# Lab Constants

Single source of truth for lab identifiers (domain, hosts, IPs, DHCP/DNS).

- **Machine-readable (canonical):** `baseline-manifest.yml` → `baseline.environment`
- **Human-readable:** this file

## Identity
- Domain (FQDN): `example.local`
- Domain (NetBIOS): `EXAMPLE`

## Hosts
- DC: `dc01.example.local` (hostname `DC01`) — `10.10.10.10`
- Client: `CL01` — DHCP lease `10.10.10.50`

## Network
- Subnet: `10.10.10.0/24` (mask `255.255.255.0`)
- DNS server: `10.10.10.10`
- Default gateway: **not configured** (blank in this lab)

## DHCP (scope)
- ScopeId: `10.10.10.0`
- Range: `10.10.10.50` – `10.10.10.200`
- Lease duration: `8 days`
- Options:
  - 003 Router: *(not set)*
  - 006 DNS servers: `10.10.10.10`
  - 015 DNS domain name: `example.local`

## DNS
- Zones: `example.local`, `_msdcs.example.local`
- SYSVOL paths: `\\dc01\SYSVOL`, `\\example.local\SYSVOL`

## Verification commands (client)
```powershell
ipconfig /all
nslookup dc01.example.local
nltest /dsgetdc:example.local
```
