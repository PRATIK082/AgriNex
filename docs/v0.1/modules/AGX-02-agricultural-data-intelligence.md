# AGX-02 — Agricultural Data Intelligence

## Purpose
Ingest, normalize, qualify and catalogue agricultural data.

## Functional requirements
- AGX-02-FR-001: Register source/license/owner/cadence
- AGX-02-FR-002: ingest event and ingestion times, unit, CRS and provenance
- AGX-02-FR-003: validate schema/unit/time/coordinates
- AGX-02-FR-004: detect duplicates/missingness/outliers/staleness
- AGX-02-FR-005: preserve raw source
- AGX-02-FR-006: quality flags
- AGX-02-FR-007: replay-safe idempotency
- AGX-02-FR-008: enforce consent/license/tenant policy.

## Data ownership and interfaces
Own Source, Dataset, Observation, QualityAssessment. Consumes device, weather, satellite, market, lab and manual feeds.

## Acceptance, safety and security
Replay safely; preserve raw evidence; reproducible transformations; no cross-tenant or unlicensed redistribution.
