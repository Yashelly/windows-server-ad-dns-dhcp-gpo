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
- `00-overview/` -> architecture + operating model
- `01-environment-build/` -> lab prerequisites and VM setup notes
- `02-ad-ds/` -> AD DS setup (role install, post-promotion state)
- `03-dns/` -> DNS configuration and checks
- `04-dhcp/` -> DHCP scope + lease validation
- `05-gpo-hardening/` -> pilot GPO (user restriction example)
- `06-validation/` -> end-to-end verification steps
- `07-ops-runbooks/` -> incident-style operational notes
- `99-evidence/` -> sanitized screenshots + evidence map

Optional expansion modules (documentation-first; evidence may be added later):
- `08-file-services/` -> SMB shares + NTFS permissions (example incident notes)
- `09-backup-recovery/` -> basic backup/recovery approach for the lab

Auxiliary folders:
- `.github/`
- `incidents/`
- `proposals/`
- `ticket-notes/`
- `scripts/`
- `templates/`
- `tools/`

## Navigation
- Start here: `START-HERE.md`
- Architecture: `00-overview/architecture.md`
- Validation steps: `06-validation/README.md`
- Evidence index: `99-evidence/README.md` + `99-evidence/EVIDENCE-MAP.md`
- Status tracker: `STATUS.md`

## Sanitization
Publishing rules: `sanitization.md`.

## Quick facts
- Domain: `example.local` (NetBIOS: `EXAMPLE`) - lab-only placeholder
- Subnet: `10.10.10.0/24`
- DC: `DC01` (static IP `10.10.10.10`)
- Client: `CL01` (DHCP lease shown in evidence)
