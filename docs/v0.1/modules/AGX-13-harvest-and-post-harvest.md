# AGX-13 — Harvest and Post-Harvest

## Purpose
Harvest readiness, lot, quality, storage and loss evidence.

## Functional requirements
- AGX-13-FR-001: Maturity estimate with uncertainty
- AGX-13-FR-002: harvest window vs weather/labor/machine/market
- AGX-13-FR-003: operation/time/equipment/operator
- AGX-13-FR-004: lot weight/moisture/quality method/calibration
- AGX-13-FR-005: genealogy through handling/storage/dispatch
- AGX-13-FR-006: crop-specific storage monitoring
- AGX-13-FR-007: losses/rejects/spoilage
- AGX-13-FR-008: forecast vs measured yield reconciliation.

## Data ownership and interfaces
Own HarvestPlan, HarvestLot, QualityMeasurement, StorageTelemetry; consumes AGX-01/02/03/12/14.

## Acceptance, safety and security
Lot traceability and mass-balance tests. No guaranteed yield/quality claims.
