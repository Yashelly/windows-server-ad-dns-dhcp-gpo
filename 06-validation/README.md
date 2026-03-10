# Validation

## Goal
Confirm end-to-end functionality:
- Client `CL01` is domain-joined and uses `DC01` as logon server
- DHCP issues a lease and points DNS to the domain controller
- DNS resolution works for domain hostnames
- Pilot GPO is applied and enforces the intended restriction

## Implementation summary
- Validation is performed from the domain-joined client `CL01` using built-in command-line checks and visible policy outcomes.
- The validation set confirms identity (`whoami`, `%logonserver%`), network configuration (`ipconfig /all`), policy application (`gpresult`), and DNS resolution (`nslookup`).

## Checks
Expected checks:
```cmd
whoami
echo %logonserver%
ipconfig /all
gpresult /r
nslookup dc01.example.local
```

## Expected results

- whoami returns a domain user context
- %logonserver% resolves to \\DC01
- ipconfig /all shows DHCP lease details and DNS = 10.10.10.10
- gpresult /r shows the pilot GPO under applied user policies
- nslookup dc01.example.local resolves to 10.10.10.10

## Planned exports

- dcdiag summary
- gpresult /h
- repadmin /replsummary (single-DC lab: minimal but still valid reference)
- additional ipconfig /all screenshot or text export

## Rollback
If validation fails after a recent change:
- revert the most recent GPO or DHCP/DNS change
- re-check domain DNS settings on the client
- re-run gpupdate /force
- use the relevant runbook in ../07-ops-runbooks/

## Evidence
Reference IDs are tracked in:
- ../99-evidence/EVIDENCE-MAP.md