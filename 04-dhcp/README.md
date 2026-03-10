# DHCP

## Goal
Provide automatic IP configuration for clients on the lab subnet `10.10.10.0/24` and validate that leases are issued correctly.

## Implementation summary
- Installed and authorized **DHCP Server** on `DC01`
- Created IPv4 scope for `10.10.10.0/24`
- Verified an active lease for `CL01` and confirmed the client received configuration via DHCP

## Validation
Validation confirms DHCP lease issuance and client configuration:
- `CL01` receives a lease within the configured pool (`10.10.10.50-10.10.10.200`).
- `ipconfig /all` on `CL01` shows:
  - DHCP enabled and DHCP server `10.10.10.10`
  - DNS suffix `example.local`
  - DNS server `10.10.10.10`
  - Default gateway *(blank in this lab)*
- The DHCP console on `DC01` shows an active lease for `CL01`.

## Rollback
Rollback is performed by reverting DHCP configuration:
- Disable/de-authorize the DHCP service and remove the lab scope if it was created incorrectly.
- Restore a pre-change snapshot of `DC01` if the environment needs to return to a known-good baseline.

## Evidence
- `EVD-DHCP-001_scope.png` -> DHCP scope
- `EVD-DHCP-002_address-leases.png` -> active lease for `CL01`
- `EVD-LAB-002_ipconfig-cl01.png` -> client `ipconfig /all` (DHCP enabled + DNS points to `DC01`)

## Planned
- Scope options capture (DNS server / default gateway) -> tracked in `STATUS.md`
- Reservation example -> tracked in `STATUS.md`
