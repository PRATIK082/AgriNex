# AGX-07 — Irrigation Intelligence

## Purpose
Water-balance-informed planning, telemetry and outcome verification.

## Functional requirements
- AGX-07-FR-001: Record sensor calibration/source/quality
- AGX-07-FR-002: model irrigation zones/hydraulic topology/pumps/valves
- AGX-07-FR-003: document crop/soil/weather assumptions
- AGX-07-FR-004: recommendation includes volume/depth/duration/uncertainty
- AGX-07-FR-005: check water/pressure/weather/restrictions
- AGX-07-FR-006: human approval and edge interlocks
- AGX-07-FR-007: distinguish schedule/command/ack/flow/outcome
- AGX-07-FR-008: detect valve/leak/dry-run/comms faults.

## Data ownership and interfaces
Own IrrigationPlan, ValveCommand, WaterTelemetry, IrrigationOutcome; consumes AGX-01/02/03/04.

## Acceptance, safety and security
Fault-injection tests sensor dropout and valve failure. Cloud recommendation cannot energize valve.
