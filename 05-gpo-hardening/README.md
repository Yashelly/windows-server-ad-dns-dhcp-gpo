# GPO hardening (pilot example)

## Goal
Demonstrate basic Group Policy management by deploying a **user** restriction policy to a pilot OU.

Policy example: block access to **Control Panel** and **Settings** for users in `PilotUsers`.

## Implementation summary
- Created a pilot OU (`PilotUsers`)
- Linked `GPO-USER-Prohibit-Control-Panel` to the pilot OU
- Enabled policy:
  - `User Configuration -> Policies -> Administrative Templates -> Control Panel -> Prohibit access to Control Panel and PC settings` = **Enabled**

## Evidence
- `EVD-GPO-001_linked-gpo-to-ou-pilotusers.png` -> GPO linked to OU
- `EVD-GPO-002_prohibit-controlpanel-enabled.png` -> setting enabled
- `EVD-VAL-003_controlpanel-blocked.png` -> client behavior (restriction dialog)
- `EVD-VAL-001_gpresult-user.png` -> applied GPO confirmation (`gpresult`)

## Notes
- This is a user-targeted example policy. Computer-targeted policies can be added later as part of a baseline set (see `ROADMAP.md`).
