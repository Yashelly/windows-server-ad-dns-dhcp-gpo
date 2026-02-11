# START HERE

Entry point for the lab build documentation and proof artifacts.

## What is implemented (v0.1.0)
- AD DS + DNS + DHCP on `DC01`
- Client `CL01` domain join
- Pilot OU (`PilotUsers`) with a sample user policy (Control Panel restriction)
- Validation proof: `whoami`, `%logonserver%`, `gpresult`, blocked UI action

## Where to look
1. Architecture and assumptions -> `00-overview/architecture.md`
2. Build steps (high level) -> `01-environment-build/README.md`
3. Service modules -> `02-ad-ds/`, `03-dns/`, `04-dhcp/`, `05-gpo-hardening/`
4. End-to-end validation -> `06-validation/README.md`
5. Evidence inventory -> `99-evidence/EVIDENCE-MAP.md` (screenshots are in `99-evidence/screenshots/`)
6. Status and backlog -> `STATUS.md`

## Evidence pack
Primary proof artifacts:
- Lab network (DC01 + CL01 IP config) -> `EVD-LAB-001_*`, `EVD-LAB-002_*`
- AD DS -> `EVD-AD-001_*` .. `EVD-AD-004_*`
- DNS -> `EVD-DNS-001_*`, `EVD-DNS-002_*`
- DHCP -> `EVD-DHCP-001_*`, `EVD-DHCP-002_*`
- GPO -> `EVD-GPO-001_*`, `EVD-GPO-002_*`
- Validation -> `EVD-VAL-001_*` .. `EVD-VAL-003_*`
