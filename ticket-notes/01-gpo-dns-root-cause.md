Symptoms: Policies not applied on W11-CL01; gpresult missing expected GPO.
Evidence: DNS misconfigured; nltest fails; GroupPolicy/Operational errors.
Root cause: Wrong DNS -> DC discovery failure -> GPO processing failure.
Fix: Set DNS to DC01, flushdns, gpupdate.
Validation: nltest ok; gpresult ok; no new GPO errors.
