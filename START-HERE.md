# START HERE

Entry point for the lab build documentation and proof artifacts.

## What is implemented (v0.1.1)
- AD DS + DNS + DHCP on `DC01`
- Client `CL01` domain join
- Pilot OU (`PilotUsers`) with a sample user policy (Control Panel restriction)
- Validation proof: `whoami`, `%logonserver%`, `gpresult`, blocked UI action

## Where to look
1. Architecture and assumptions -> `00-overview/architecture.md`
2. Build summary (high level) -> `01-environment-build/README.md`
3. Service modules -> `02-ad-ds/`, `03-dns/`, `04-dhcp/`, `05-gpo-hardening/`
4. End-to-end validation -> `06-validation/README.md`
5. Evidence index -> `99-evidence/EVIDENCE-MAP.md`
6. Runbooks -> `07-ops-runbooks/`

## What is not yet fully evidenced
- File services module (`08-file-services/`)
- Backup/recovery module (`09-backup-recovery/`)
- Some planned exports listed in `06-validation/README.md`

## Current state
- Baseline status -> `STATUS.md`
- Planned next steps -> `ROADMAP.md`