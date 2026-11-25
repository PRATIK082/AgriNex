# AgriNex V0.1 System Requirements
M=mandatory foundation; S=subsequent. Verify T=test, I=inspection, D=demonstration.

| ID | Requirement | Priority | Verify |
|---|---|---|---|
| AGX-SYS-001 | Represent tenant, farm, field, zone and asset using stable IDs. | M | T |
| AGX-SYS-002 | Tenant-owned records carry tenant identity and enforce ownership. | M | T |
| AGX-SYS-003 | Geometries declare CRS; API GeoJSON uses WGS84/EPSG:4326. | M | T |
| AGX-SYS-004 | Observations carry value, unit, observed time, source, quality and provenance. | M | T |
| AGX-SYS-005 | Distinguish observation/event time from ingestion time. | M | T |
| AGX-SYS-006 | Version APIs/schemas and document compatibility policy. | M | I |
| AGX-SYS-007 | Modules interact through contracts, not direct cross-domain table access. | M | I |
| AGX-SYS-008 | Trace requirements to design, implementation and verification evidence. | M | I |
| AGX-SYS-009 | Reproducible local setup and automated CI. | M | D |
| AGX-SYS-010 | Demonstrate farm, field and observation create/list workflow. | M | T/D |
| AGX-SYS-011 | Preserve source, method, quality and uncertainty when available. | M | T |
| AGX-SYS-012 | Reject malformed payloads, invalid coordinates and missing units. | M | T |
| AGX-SYS-013 | Separate measurement, estimate, recommendation, command, acknowledgement and outcome. | M | I |
| AGX-SYS-014 | Device commands are authorized, bounded, expiring, idempotent and edge-validated. | S | T |
| AGX-SYS-015 | Cloud AI cannot bypass local safety controller, E-stop or interlocks. | M | I |
| AGX-SYS-016 | Consequential changes and approvals have auditable history. | S | T |
| AGX-SYS-017 | Data export honors tenant, ownership, consent and license. | S | T |
| AGX-SYS-018 | Offline edge events reconcile without silent conflict overwrite. | S | T |
| AGX-SYS-019 | Expose health/readiness and structured telemetry. | M | T |
| AGX-SYS-020 | Production claims require security, safety, agronomy, legal and field validation gates. | M | I |

Quality attributes: least privilege; explicit units/CRS/time; reproducible calculations; replaceable device adapters; offline tolerance; documented performance budgets after workload discovery; independent machine safety.
