# AGX-08 — Nutrition and Fertigation

## Purpose
Evidence-based crop nutrition planning and application traceability.

## Functional requirements
- AGX-08-FR-001: Bind crop/stage/soil/tissue/water context
- AGX-08-FR-002: define nutrient unit/basis
- AGX-08-FR-003: distinguish diagnosis/model/expert conclusion
- AGX-08-FR-004: verify approved product label/jurisdiction/expiry
- AGX-08-FR-005: draft plan with evidence/uncertainty
- AGX-08-FR-006: compatibility only with validated evidence
- AGX-08-FR-007: record actual product lot/amount/area/time/calibration
- AGX-08-FR-008: reconcile application and response.

## Data ownership and interfaces
Own NutrientPlan, ProductProfile, ApplicationRecord; consumes soil/crop analysis and approved FertiNex exports.

## Acceptance, safety and security
Unit/basis conversion tests. No AI-generated formulation or dose automatically approved.

## V0.2 extension — plant-stage nutrition intelligence
Nutrition plans must integrate soil tests, tissue tests, water quality, crop/cultivar, plant age and phenological stage, GDD, weather, previous nutrient applications, yield target and approved product/label constraints. Use locally validated STCR/ICAR/state recommendations; expose evidence, assumptions and uncertainty; require human approval. See [full capability specification](../../v0.2/SOIL_SEED_LEAF_PLANT_INTELLIGENCE.md).
