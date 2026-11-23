# V0.1 Architecture
Use a modular monolith: API/application layer, domain modules, adapters, PostgreSQL/PostGIS system of record, object storage and event/outbox abstraction. ROS 2 and real-time device control remain at edge, not cloud request path.

Layers: experience/API → use cases/authorization → domain rules → persistence/integration adapters → edge/robot runtime. Weather/satellite/market feeds enter through provenance-aware ingestion. Independent safety controller governs actuators.

Invariants: domain-owned data; stable IDs and versioned contracts; UTC timestamps; GeoJSON/EPSG:4326 boundary; explicit units; measured facts ≠ estimates ≠ recommendations ≠ commands ≠ acknowledgements ≠ verified outcomes; no cloud-to-actuator direct path; local safe state during outage; AI cannot override safety or approve its own high-impact output.
