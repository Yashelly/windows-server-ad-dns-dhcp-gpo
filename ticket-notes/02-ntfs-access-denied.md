# Ticket note (example, synthetic)

This ticket note is a **synthetic example** written for portfolio purposes.
Hostnames and object names may be placeholders and are not required to match the lab naming conventions.

Symptoms: User cannot access \\fs01\Finance ("Access Denied").
Evidence: user not in FIN-RW; NTFS allows FIN-RW; share perms OK.
Root cause: Missing group membership.
Fix: Added to FIN-RW; user re-login.
Validation: Access OK; file create/read tested.
