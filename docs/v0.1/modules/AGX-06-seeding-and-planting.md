# AGX-06 — Seeding and Planting

## Purpose
Plan planting and preserve as-planted records.

## Functional requirements
- AGX-06-FR-001: Capture crop/variety/seed lot/treatment/viability provenance
- AGX-06-FR-002: target population/spacing/depth with basis/units
- AGX-06-FR-003: validate planter capability/calibration
- AGX-06-FR-004: version row/coverage plan
- AGX-06-FR-005: record as-planted position/rate/depth
- AGX-06-FR-006: compare planned/measured population
- AGX-06-FR-007: record overrides/refill/lot changes
- AGX-06-FR-008: link emergence.

## Data ownership and interfaces
Own PlantingPlan, SeedLot, AsPlantedEvent; consumes AGX-01/02/03/05/11/15.

## Acceptance, safety and security
Simulation links plan to seed lot and telemetry. No unvalidated automatic real-machine rate control.
