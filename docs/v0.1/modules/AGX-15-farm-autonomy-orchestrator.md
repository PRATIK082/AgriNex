# AGX-15 — Farm Autonomy Orchestrator

## Purpose
Coordinate plans and fleets under resource constraints and safety boundaries.

## Functional requirements
- AGX-15-FR-001: Maintain objectives/dependencies/horizon
- AGX-15-FR-002: consume recommendations with source/expiry/uncertainty/approval
- AGX-15-FR-003: resolve water/machine/labor/energy/weather conflicts
- AGX-15-FR-004: create proposed plans without dispatch by default
- AGX-15-FR-005: risk-based authorization
- AGX-15-FR-006: expiry/idempotency/geofence/capability checks
- AGX-15-FR-007: track mission/outcomes
- AGX-15-FR-008: pause/abort on stale data/comms/safety events
- AGX-15-FR-009: audit rationale
- AGX-15-FR-010: never override E-stop.

## Data ownership and interfaces
Own FarmPlan, Task, Authorization, MissionDispatch, Outcome; consumes AGX-01…14.

## Acceptance, safety and security
Deterministic scheduling and fault injection. Orchestrator is not a safety controller.
