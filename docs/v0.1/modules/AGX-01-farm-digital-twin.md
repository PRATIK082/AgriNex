# AGX-01 — Farm Digital Twin

## Purpose
Canonical tenant/farm/field/zone/asset/crop-cycle context.

## Functional requirements
- AGX-01-FR-001: Create/list farms
- AGX-01-FR-002: register field polygons with CRS/source
- AGX-01-FR-003: manage zones
- AGX-01-FR-004: register assets/capabilities
- AGX-01-FR-005: associate crop cycles
- AGX-01-FR-006: spatial queries
- AGX-01-FR-007: preserve geometry revisions
- AGX-01-FR-008: publish change events.

## Data ownership and interfaces
Own Farm, Field, Zone, Asset, CropCycle. REST farm/field resources. Consumes GIS, observations and crop plans.

## Acceptance, safety and security
Reject malformed geometry and invalid WGS84; enforce ownership. Farm boundary is not automatically a certified robot geofence.
