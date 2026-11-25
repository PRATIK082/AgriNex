# AGX-05 — Land Preparation

## Purpose
Plan and record tillage, leveling and bed preparation.

## Functional requirements
- AGX-05-FR-001: Define operation/geometry/implement/capability
- AGX-05-FR-002: assess soil/slope/obstacles/weather
- AGX-05-FR-003: version coverage/path plan
- AGX-05-FR-004: require operator authorization
- AGX-05-FR-005: record planned vs executed track/settings
- AGX-05-FR-006: detect missed/overlap area
- AGX-05-FR-007: preserve calibration
- AGX-05-FR-008: abort/recovery workflow.

## Data ownership and interfaces
Own OperationPlan/ExecutionTrack; consumes AGX-01/02/04/11/15.

## Acceptance, safety and security
Simulation validates coverage/boundaries. Real actuation needs machine risk assessment and local safety.
