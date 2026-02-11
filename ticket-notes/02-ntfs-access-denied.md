Symptoms: User cannot access \\FS01\Finance ("Access Denied").
Evidence: user not in FIN-RW; NTFS allows FIN-RW; share perms OK.
Root cause: Missing group membership.
Fix: Added to FIN-RW; user re-login.
Validation: Access OK; file create/read tested.
