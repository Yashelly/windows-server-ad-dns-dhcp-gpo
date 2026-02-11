# Sanitization policy

This repository is prepared for public sharing. Evidence is sanitized to remove personal or environment-identifiable data while keeping enough technical context to review the build.

## Allowed to remain (lab context)
- Lab domain: `example.local` (NetBIOS: `EXAMPLE`)
- Lab hostnames: `DC01`, `CL01`
- RFC1918 subnet: `10.10.10.0/24` (lab-only addressing)

## Must be removed
- Real domains/UPNs, emails, tenant identifiers, external IPs
- Passwords, secrets, private keys, certificates
- Object IDs / GUIDs that link back to a real environment
- Device serial numbers, unique hardware identifiers (when avoidable)

## Folder policy
- `reports/` is a local workspace for raw outputs and is gitignored.
- Sanitized exports intended for publishing belong in `99-evidence/exports/`.
- `.gitkeep` files are used to keep empty folders versioned without committing raw data.
