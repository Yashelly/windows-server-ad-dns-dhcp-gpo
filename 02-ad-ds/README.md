# AD DS (Domain Controller)

## Goal
Deploy **Active Directory Domain Services** on `DC01` by creating a new forest/domain (`example.local`) and confirming that the domain is operational.

## Implementation summary
- Installed **Active Directory Domain Services** role on `DC01`
- Promoted the server to a domain controller (new forest)
- Verified domain visibility in **Active Directory Users and Computers** and Server Manager
- Noted the DNS delegation warning during prerequisites check (expected for an isolated lab)

## Evidence
- `EVD-AD-001_adds-role.png` -> AD DS role install
- `EVD-AD-002_domain-visible-aduc.png` -> domain/OU visible in ADUC
- `EVD-AD-003_prereq-dns-delegation.png` -> prerequisites check note
- `EVD-AD-004_servermanager-after-promo.png` -> roles after promotion

## Notes
- The prerequisites warning about DNS delegation is common when no parent DNS zone exists (typical in a lab without upstream DNS infrastructure).
