# 01-environment-build

## Goal
Establish the lab foundation: VM provisioning, network plan, and base OS configuration for `DC01` and `CL01`.

## Implementation summary (lab)
- Two VMs were provisioned:
  - `DC01` (Windows Server)
  - `CL01` (Windows client)
- `DC01` was configured with a static IPv4 configuration aligned to `LAB-CONSTANTS.md`:
  - IPv4: `10.10.10.10/24`
  - DNS: `10.10.10.10` (self, single-DC lab)
  - Default gateway: *(not configured in this lab)*
- `CL01` was kept DHCP-enabled and receives configuration after DHCP is deployed on `DC01`.

## Validation
Validation is based on captured configuration outputs:
- `ipconfig /all` on `DC01` confirms the static IPv4 configuration and DNS setting.
- `ipconfig /all` on `CL01` confirms DHCP is enabled and that the lease and DNS settings are received from `DC01`.

## Rollback
Rollback for this phase is performed by reverting network configuration to the previous state:
- `DC01`: revert IPv4 settings back to DHCP (or restore a pre-change VM snapshot).
- `CL01`: no rollback is required unless static settings were introduced; in that case, revert the NIC to DHCP.

## Evidence
- `EVD-LAB-001_ipconfig-dc01.png` (Captured)
- `EVD-LAB-002_ipconfig-cl01.png` (Captured)
