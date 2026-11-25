# AGX-10 — Aerial Robotics

## Purpose
Drone capability, scouting/mapping mission and imagery metadata.

## Functional requirements
- AGX-10-FR-001: Register aircraft/payload/firmware/battery/calibration/envelope
- AGX-10-FR-002: check jurisdiction/pilot/airspace/weather/site
- AGX-10-FR-003: georeferenced survey plan and GSD assumptions
- AGX-10-FR-004: operator preflight approval
- AGX-10-FR-005: telemetry/flight log/images/anomalies
- AGX-10-FR-006: validate CRS/time/lineage
- AGX-10-FR-007: separate survey from application
- AGX-10-FR-008: manufacturer-defined lost-link/battery/geofence response.

## Data ownership and interfaces
Own AerialMission, FlightTelemetry, ImageryAsset, PilotApproval; consumes AGX-01/02/12/15.

## Acceptance, safety and security
Simulation validates bounds/metadata. Software plan is not flight authorization or safety override.
