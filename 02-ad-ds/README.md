# AD DS (Domain Controller)

## Goal
Deploy **Active Directory Domain Services** on `DC01` by creating a new forest/domain (`example.local`) and confirming that the domain is operational.

## Implementation summary
- Installed **Active Directory Domain Services** role on `DC01`
- Promoted the server to a domain controller (new forest)
- Verified domain visibility in **Active Directory Users and Computers** and Server Manager
- Noted the DNS delegation warning during prerequisites check (expected for an isolated lab)

## Validation
Validation confirms that the domain controller promotion completed successfully:
- The `example.local` domain is visible in **Active Directory Users and Computers**.
- **Server Manager** indicates `DC01` hosts AD DS and DNS roles.
- Basic domain health checks (e.g., `dcdiag`) are expected to complete without critical errors in an isolated lab.

## Rollback
Rollback is performed using a lab-safe approach:
- Preferred: restore a pre-promotion VM snapshot of `DC01`.
- Alternative: demote the domain controller (remove AD DS role) and remove the `example.local` forest, then rebuild from a clean state.

## Evidence
- `EVD-AD-001_adds-role.png` -> AD DS role install
- `EVD-AD-002_domain-visible-aduc.png` -> domain/OU visible in ADUC
- `EVD-AD-003_prereq-dns-delegation.png` -> prerequisites check note
- `EVD-AD-004_servermanager-after-promo.png` -> roles after promotion

## Notes
- The prerequisites warning about DNS delegation is common when no parent DNS zone exists (typical in a lab without upstream DNS infrastructure).
