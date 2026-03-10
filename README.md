# Windows Server Lab - AD DS, DNS, DHCP, GPO (from scratch)

This repository documents a small Windows Server lab built from scratch and validated end-to-end:
- Active Directory Domain Services (AD DS)
- DNS
- DHCP
- Group Policy (pilot OU + sample user restriction)
- Domain join + policy validation from a Windows client

The focus is **hands-on implementation + verifiable evidence** (sanitized screenshots) and short ops-style notes.

## Repository structure
Core scope (captured evidence in `99-evidence/`):
- `00-overview/` - architecture, naming, assumptions, operating model
- `01-environment-build/` - VM/network setup and initial server prep
- `02-ad-ds/` - domain controller promotion and AD DS verification
- `03-dns/` - DNS zone/record validation
- `04-dhcp/` - DHCP scope/options and lease validation
- `05-gpo-hardening/` - pilot OU + sample user GPO
- `06-validation/` - end-to-end validation from client side
- `07-ops-runbooks/` - short troubleshooting runbooks

Expansion modules (documentation-first, evidence pending):
- `08-file-services/` - SMB shares + NTFS permissions model
- `09-backup-recovery/` - basic backup/recovery notes for the lab

Supporting repo files:
- `99-evidence/` - screenshot index and proof map
- `templates/` - repo documentation templates
- `tools/` - simple consistency checks
- `STATUS.md` - implementation/evidence maturity
- `ROADMAP.md` - next planned increments
- `START-HERE.md` - quick entry point
- `baseline-manifest.yml` - compact baseline scope + evidence policy

## Quick facts
- Domain: `example.local`
- DC: `DC01` (`10.10.10.10`)
- Client: `CL01`
- DHCP scope: `10.10.10.50-10.10.10.200`
- Pilot OU: `PilotUsers`
- Sample GPO: prohibit access to Control Panel / PC settings

For environment constants, see:
- `LAB-CONSTANTS.md`
- `baseline-manifest.yml`

## Evidence style
Evidence is sanitized and indexed in:
- `99-evidence/EVIDENCE-MAP.md`

## Current release
See:
- `START-HERE.md`
- `STATUS.md`
- `ROADMAP.md`