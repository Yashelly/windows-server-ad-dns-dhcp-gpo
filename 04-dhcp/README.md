# DHCP

## Goal
Provide automatic IP configuration for clients on the lab subnet `10.10.10.0/24` and validate that leases are issued correctly.

## Implementation summary
- Installed and authorized **DHCP Server** on `DC01`
- Created IPv4 scope for `10.10.10.0/24`
- Verified an active lease for `CL01` and confirmed the client received configuration via DHCP

## Evidence
- `EVD-DHCP-001_scope.png` -> DHCP scope
- `EVD-DHCP-002_address-leases.png` -> active lease for `CL01`
- `EVD-LAB-002_ipconfig-cl01.png` -> client `ipconfig /all` (DHCP enabled + DNS points to `DC01`)

## Planned
- Scope options capture (DNS server / default gateway) -> tracked in `STATUS.md`
- Reservation example -> tracked in `STATUS.md`
