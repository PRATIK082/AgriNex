# AGX-09 — Crop Protection

## Purpose
Scouting, diagnosis evidence and integrated pest-management support.

## Functional requirements
- AGX-09-FR-001: Capture organism/confidence/life-stage/location/crop-stage/image
- AGX-09-FR-002: distinguish suspected vs confirmed
- AGX-09-FR-003: thresholds scoped to crop/region/method/source
- AGX-09-FR-004: document IPM/nonchemical options
- AGX-09-FR-005: verify current registration/label/crop/use
- AGX-09-FR-006: qualified approval
- AGX-09-FR-007: record application/lot/operator/weather/buffers
- AGX-09-FR-008: resistance and beneficial-organism constraints.

## Data ownership and interfaces
Own ScoutObservation, Diagnosis, IPMRecommendation, ProtectionEvent; consumes AGX-01/02/12.

## Acceptance, safety and security
Uncertain CV detection abstains; block prohibited/unverified use. No autonomous pesticide selection/mixing/spraying.
