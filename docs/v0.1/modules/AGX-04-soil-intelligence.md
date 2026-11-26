# AGX-04 — Soil Intelligence

## Purpose
Soil profiles, sampling, laboratory results and spatial variability.

## Functional requirements
- AGX-04-FR-001: Record sample location/depth/method/date/collector
- AGX-04-FR-002: chain of custody
- AGX-04-FR-003: result with unit/detection limit/uncertainty/lab
- AGX-04-FR-004: distinguish measurement from interpolation
- AGX-04-FR-005: method-tag pH/EC/texture/carbon/nutrients
- AGX-04-FR-006: spatial layer CRS/resolution/source
- AGX-04-FR-007: crop/season/depth-specific interpretation
- AGX-04-FR-008: stale/conflict flags.

## Data ownership and interfaces
Own SoilProfile, SoilSample, LabResult, SoilLayer; consumes GIS/LIMS; serves AGX-03/07/08.

## Acceptance, safety and security
Preserve method, depth, units and provenance. No universal threshold without crop/region/method context.

## V0.2 extension — comprehensive soil testing
Support the Indian SHC panel (available N/P/K/S; Zn/Fe/Cu/Mn/B; pH/EC/OC) plus extensible chemical, physical, hydrological and biological panels. Add device/lab evidence classes, calibration, sample preparation, method, depth, uncertainty, chain of custody and paired reference-lab validation. Never claim every parameter is measured directly by a single probe. See [full capability specification](../../v0.2/SOIL_SEED_LEAF_PLANT_INTELLIGENCE.md).
