# Architecture

## Components
- **DC01** (Windows Server) -> AD DS + DNS + DHCP + Group Policy Management
- **CL01** (Windows client) -> domain-joined workstation used for validation

## Network plan
- Subnet: `10.10.10.0/24`
- DC01: `10.10.10.10` (static, also DNS server)
- CL01: DHCP lease (see evidence)

## Directory / DNS
- AD domain: `example.local` (NetBIOS: `EXAMPLE`)
- DNS forward lookup zone: `example.local`
- Records validated from CL01 via `nslookup`

## DHCP
- Scope: `10.10.10.0/24`
- Active client lease captured for `CL01` (see `EVD-DHCP-002_address-leases.png`)

## GPO model
- OUs:
  - `PilotUsers` (pilot users)
  - `Workstations` (computer objects; reserved for expansion)
- Example policy:
  - `GPO-USER-Prohibit-Control-Panel` linked to `PilotUsers`
