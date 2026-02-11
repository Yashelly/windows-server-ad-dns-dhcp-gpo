# DNS

## Goal
Provide name resolution for the AD domain (`example.local`) and validate lookups from a domain-joined client.

## Implementation summary
- DNS role is installed as part of the domain controller promotion on `DC01`
- Forward lookup zone for `example.local` exists and contains host records for lab systems
- Validated resolution of `dc01.example.local` using `nslookup` from `CL01`

## Evidence
- `EVD-DNS-001_forward-zone-example-local.png` -> DNS Manager forward zone view
- `EVD-DNS-002_nslookup-dc01.png` -> `nslookup` validation

## Notes
- Reverse lookup zone and PTR validation are tracked as planned in `STATUS.md` if needed for the lab scenario.
