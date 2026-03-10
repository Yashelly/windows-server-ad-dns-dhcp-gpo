# Naming standards

## Hosts
- `DC01` -> domain controller
- `CL01` -> domain-joined client

## Network (lab)
- Subnet: `10.10.10.0/24`
- `DC01`: `10.10.10.10` (static)
- DHCP pool: `10.10.10.50-10.10.10.200`
- Default gateway: *(not configured in this lab)*

## Formatting conventions
- Narrative text uses hostnames as `DC01` / `CL01`.
- FQDN and UNC paths use lowercase, e.g. `dc01.example.local`, `\\dc01\SYSVOL`.

## Evidence
Evidence references are tracked in `templates/evidence-naming.md`.
