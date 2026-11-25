# Common Data Model
Entities: Tenant, Farm, Field, Zone, Asset, CropCycle, Observation, Sample, Recommendation, Mission, Command, Acknowledgement, Telemetry, Outcome, Provenance, Consent and AuditEvent.

Common fields: id, tenant_id, created_at, schema_version, trace_id; updates add updated_at. Measurements include observed_at, value, unit, quality, optional uncertainty. Spatial records include geometry, CRS and geometry_source.

Use UCUM-compatible units where practical; preserve source unit and conversion method. Never silently convert nutrient basis, concentration, mass/area or moisture basis. Sensor reading is not calibrated truth; model estimate is not measurement; recommendation is not approval; command is not execution. Farm and geospatial data may be sensitive; enforce ownership, consent, retention and export controls.
