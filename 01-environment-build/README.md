# 01-environment-build

## Goal
Establish the lab foundation: VM setup, network plan, and base OS configuration for `DC01`/`CL01`.

## Implementation summary (lab)
- Provisioned two VMs:
  - `DC01` (Windows Server)
  - `CL01` (Windows client)
- Configured static IPv4 for `DC01`:
  - **Control Panel** -> **Network and Internet** -> **Network Connections**
  - **Ethernet** -> **Properties** -> **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**
  - Lab example: `10.10.10.10/24`; Preferred DNS: `10.10.10.10`
- Client `CL01` is DHCP-enabled and receives configuration after DHCP is deployed on `DC01`

## Validation performed
- `ipconfig /all` on `DC01` and `CL01`

## Evidence
- `EVD-LAB-001_ipconfig-dc01.png` (Captured)
- `EVD-LAB-002_ipconfig-cl01.png` (Captured)
