# GPO hardening (pilot example)

## Goal
Demonstrate basic Group Policy management by deploying a **user** restriction policy to a pilot OU.

Policy example: block access to **Control Panel** and **Settings** for users in `PilotUsers`.

## Implementation summary
- Created a pilot OU (`PilotUsers`)
- Linked `GPO-USER-Prohibit-Control-Panel` to the pilot OU
- Enabled the Administrative Templates user policy **"Prohibit access to Control Panel and PC settings"**

## Validation
Validation confirms policy application from a domain-joined client:
- `gpupdate /force` completes successfully
- `gpresult /r` shows the expected GPO under user policy scope
- Attempting to open Control Panel or Windows Settings is blocked for the test user

## Rollback
Rollback is straightforward and low risk:
- unlink the pilot GPO from the OU, or
- set the policy back to **Not Configured**

## Evidence
- GPMC screenshot showing OU + linked GPO
- Policy setting screenshot (enabled)
- Client-side blocked action screenshot
- `gpresult` snippet or screenshot

See also:
- `../99-evidence/EVIDENCE-MAP.md`
- `../07-ops-runbooks/gpo-not-applying.md`