# Prerequisites

## Lab assumptions
- Hypervisor: Hyper-V / VMware / VirtualBox
- Two VMs:
  - `DC01` (Windows Server)
  - `CL01` (Windows client)

## Networking
- `DC01` uses static IPv4 configuration aligned to the canonical constants.
- `CL01` remains DHCP-enabled and receives scope options after DHCP is deployed on `DC01`.

Canonical environment constants are defined in:
- `LAB-CONSTANTS.md`
- `baseline-manifest.yml` -> `baseline.environment`

## Tools
- Server Manager roles: AD DS, DNS, DHCP
- Group Policy Management (GPMC)
