# Module Interface Specifications
REST prefix /api/v1; OpenAPI 3.1; JSON; UUID identifiers; UTC ISO-8601 timestamps; GeoJSON EPSG:4326 at public boundary; quantities include value/unit/basis; structured errors include code/message/details/trace_id; idempotency key for non-repeatable writes; events include id/type/source/subject/time/schema/tenant/trace/data. Additive optional fields are minor-compatible; breaking changes require a new major schema/API version.

| Module | Provides | Consumes |
|---|---|---|
| AGX-01 | Farm/field/zone/asset context | GIS, observations, crop plans |
| AGX-02 | Validated observations, quality, provenance | Devices, weather, satellite, manual data |
| AGX-03 | Evidence-linked recommendations | Crop, soil, weather, field data |
| AGX-04 | Soil profiles, samples, analysis | Lab, GIS, samples |
| AGX-05 | Land operation plans/outcomes | Field, soil, equipment |
| AGX-06 | Planting plans/as-planted records | Crop, seed lot, field, machinery |
| AGX-07 | Irrigation plans/water events | Moisture, weather, flow, valves |
| AGX-08 | Nutrient plans/application records | Soil/crop analysis, approved input catalogue |
| AGX-09 | Scout/diagnosis/IPM records | Pest observations, label constraints |
| AGX-10 | Aerial missions/imagery metadata | Zones, flight capability, approvals |
| AGX-11 | Ground missions/robot telemetry | Maps, capabilities, authorization |
| AGX-12 | Crop health detections/trends | Images, scouting, crop stage |
| AGX-13 | Harvest lots/quality/storage | Maturity, equipment, yield |
| AGX-14 | Market signals/forecasts | Licensed feeds, commodity IDs |
| AGX-15 | Cross-domain plans/authorization | Recommendations, device state, policies |

Command lifecycle: plan → context/freshness check → risk assessment → authorized approval → expiring dispatch → edge precondition check → local execution → acknowledgement → independent outcome verification → audit. Network acknowledgement never proves physical completion.
