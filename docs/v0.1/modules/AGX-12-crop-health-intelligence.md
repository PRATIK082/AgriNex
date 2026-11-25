# AGX-12 — Crop Health Intelligence

## Purpose
Monitor crop condition from imagery, scouting and time-series.

## Functional requirements
- AGX-12-FR-001: Record image/source/time/location/crop/stage
- AGX-12-FR-002: model/dataset/license/version/domain
- AGX-12-FR-003: detection/confidence/uncertainty/spatial extent
- AGX-12-FR-004: OOD/poor image abstention
- AGX-12-FR-005: symptom vs causal diagnosis
- AGX-12-FR-006: trends by field/zone/time
- AGX-12-FR-007: expert verification
- AGX-12-FR-008: drift/error monitoring.

## Data ownership and interfaces
Own ImageAsset, HealthDetection, CropHealthTrend; consumes AGX-01/02/10 and feeds AGX-03/09.

## Acceptance, safety and security
Local validation datasets and abstention tests. Image class alone never triggers treatment.
