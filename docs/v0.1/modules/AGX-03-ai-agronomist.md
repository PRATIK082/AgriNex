# AGX-03 — AI Agronomist

## Purpose
Evidence-linked agronomy decision support using scientific models and reviewed ML.

## Functional requirements
- AGX-03-FR-001: Require crop/variety/stage/location/season
- AGX-03-FR-002: retrieve cited authoritative evidence
- AGX-03-FR-003: separate facts/estimates/assumptions/recommendations
- AGX-03-FR-004: expose uncertainty
- AGX-03-FR-005: abstain on missing/out-of-domain context
- AGX-03-FR-006: version models/rules/prompts/corpus
- AGX-03-FR-007: expert review high-impact output
- AGX-03-FR-008: record outcomes without causal overclaim.

## Data ownership and interfaces
Own Recommendation and EvidenceBundle. Consumes AGX-01/02/04/07/08/09/12; exposes recommendation API.

## Acceptance, safety and security
Every output cites sources/context. No autonomous pesticide/fertilizer dose or machine actuation.
