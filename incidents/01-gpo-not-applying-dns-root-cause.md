# Incident record: GPO not applying due to wrong DNS (root cause demo)

Lab reproduction summary:
- Domain-joined client DNS was set to a public resolver (e.g., 8.8.8.8)

Evidence:
- `ipconfig /all`
- `nltest /dsgetdc:example.local`
- `gpresult /h`
- Event Viewer -> GroupPolicy/Operational

Root cause:
- Wrong DNS -> DC discovery fails -> GPO processing fails

Remediation:
- Restored client DNS to DC01 IP, then `ipconfig /flushdns` and `gpupdate /force`

Validation:
- `nltest` succeeded; `gpresult` showed the expected GPO; GroupPolicy errors stopped
