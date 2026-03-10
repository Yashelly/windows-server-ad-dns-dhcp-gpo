# Ticket note (example, synthetic)

This ticket note is a **synthetic example** written for portfolio purposes.
Hostnames and object names may be placeholders and are not required to match the lab naming conventions.

Symptoms: Policies not applied on W11-CL01; gpresult missing expected GPO.
Evidence: DNS misconfigured; nltest fails; GroupPolicy/Operational errors.
Root cause: Wrong DNS -> DC discovery failure -> GPO processing failure.
Fix: Set DNS to DC01, flushdns, gpupdate.
Validation: nltest ok; gpresult ok; no new GPO errors.
