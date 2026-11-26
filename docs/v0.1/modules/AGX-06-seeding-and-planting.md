# AGX-06 — Seeding, Planting and Seed Intelligence (V0.2 extension)

## Scope
Own seed-lot identity, seed quality evidence, planting operation and crop establishment records. The seed scanner is a screening device, not a statutory certification instrument.

## Requirements
- AGX-06-FR-001: Register species/crop, cultivar/hybrid, supplier, lot, production/packing date, treatment/coating, expiry, label and source documents.
- AGX-06-FR-002: Preserve representative sample identity and chain of custody.
- AGX-06-FR-003: Support purity, moisture, germination, vigour, seed health, insect damage and cultivar/genuineness test records with method/version.
- AGX-06-FR-004: Capture controlled-light seed images and derive count, dimensions, shape, colour, visible damage and uniformity with confidence and manual review.
- AGX-06-FR-005: Distinguish image screening from lab germination, viability, genetic purity and pathogen results.
- AGX-06-FR-006: Link seed lot to field, planting event, sowing/transplant date, rate, depth, spacing and equipment.
- AGX-06-FR-007: Track emergence, stand count, gaps and establishment observations.
- AGX-06-FR-008: Preserve applicable crop-specific/Indian standards and competent-lab certification references.

## Interfaces and data ownership
Own SeedLot, SeedSample, SeedTest, SeedImageAssessment, PlantingEvent and EstablishmentObservation. Consumes AGX-01 field/zone and AGX-02 provenance; provides seed/crop-cycle context to AGX-03/08/12.

## Acceptance and safety
Image classifier validation against human/lab ground truth; no germination or certification claim from appearance alone. See [Soil, Seed, Leaf & Plant Intelligence](../../v0.2/SOIL_SEED_LEAF_PLANT_INTELLIGENCE.md).
