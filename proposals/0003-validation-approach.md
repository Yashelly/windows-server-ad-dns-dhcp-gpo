# 0003 - Validation approach

## Goals
Validation is designed to answer:
- Domain services are installed and functional.
- DNS resolves correctly for domain and basic lookups.
- DHCP hands out leases in the expected scope.
- GPO applies to a domain-joined client and produces a visible outcome.

## Validation set (examples)
- Client:
  - `whoami`
  - `echo %logonserver%`
  - `gpresult /r` and/or Group Policy Results in GPMC
- Server:
  - DHCP scope configuration and active leases
  - DNS zones and records required for the domain
