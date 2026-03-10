# 00-overview

## Goals
- Keep the lab build and decisions easy to review.
- Track what is implemented vs planned.
- Keep evidence sanitized and linkable.

## Operating principles
- **Evidence-first:** captured proof lives in `99-evidence/` and is referenced by ID.
- **Modules:** each major component has its own folder with:
  - goal and implementation summary
  - validation
  - rollback
  - evidence checklist (optional)
- **Documentation:** short, operational, and easy to review.

## Overview docs
- `architecture.md` -> high-level diagram, IP plan, roles
- `decision-log.md` -> notable decisions and rationale
- `naming-standards/` -> naming used in this repo
- `operating-model/` -> folder layout, status tracking, evidence policy
- `prereqs/` -> lab prerequisites and assumptions

## Source of truth
Lab constants are canonical in:
- `baseline-manifest.yml` -> `baseline.environment`
- `LAB-CONSTANTS.md` (human-readable)

## Sanitization
Publishing rules are in `sanitization.md`.
