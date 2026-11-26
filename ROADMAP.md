# AgriNex Roadmap

Capability-based and dependency-driven; dates are not guaranteed. A stage is complete only when verification evidence is linked.

## Stage 0 — V0.1 foundation (repository increment completed)
- [x] System requirements and specifications for all 15 AGX modules.
- [x] Shared data model and interface conventions.
- [x] FastAPI farm/field/observation demonstrator and tests.
- [x] PostGIS target schema reference and local Compose service.
- [x] ROS 2/Gazebo starter scaffold.
- [x] GitHub Actions API CI; main-branch run passed 2026-11-25.
- [ ] ROS workspace and simulation still require build/runtime validation.

## Stage 1 — Engineering integrity and security (next)
- Clean documentation/repository structure and expand CI.
- Authentication, authorization and tenant isolation.
- ADRs for database migrations, spatial semantics, units, provenance, events, audit, API versioning and retention.
- Threat model, data classification, SBOM and license inventory.
**Exit:** reviewed platform architecture; no unauthenticated external deployment.

## Stage 2 — AGX-01 Digital Farm
- PostgreSQL/PostGIS integration and Alembic migrations.
- Tenant, farm, field, zone, asset and crop-cycle lifecycle.
- Geometry validation, spatial indexing/queries and defensible area calculation.
- Audit history, GeoJSON import/export and API contract tests.
**Exit:** secure, tested PostGIS digital-farm vertical slice.

## Stage 3 — AGX-02 Data Intelligence
- Source registry, ingestion, validation, normalization and provenance.
- Sensor/MQTT, weather, STAC satellite and laboratory adapters.
- Quality flags, deduplication, replay and offline reconciliation.
**Exit:** reproducible ingest-to-query pipeline with lineage.

## Stage 4 — ROS 2 and simulation
- Pinned ROS 2 Jazzy/Gazebo Harmonic environment.
- Build/test workspace in CI; TF/QoS/clock/diagnostics.
- Farm world, rover model, navigation and fault-injection scenarios.
**Exit:** reproducible headless simulation; no physical actuation.

## Stage 5 — Scientific agronomy
- Soil sampling/lab data, crop calendars and weather.
- Select and calibrate one crop model for one crop/site/season.
- Evidence-linked recommendations and expert review.
**Exit:** independent validation report and declared model domain.

## Stage 6 — Supervised farm systems
- Soil, irrigation and nutrition workflows with verified product/label constraints.
- Irrigation test rig with independent safety controller.
- Drone imagery ingestion under current jurisdictional approvals.
**Exit:** supervised pilot with measured outcomes and safety procedures.

## Stage 7 — Robotics and fleet autonomy
- Machine capability adapters, missions, teleoperation and safety case.
- SIL/HIL, obstacle/fault tests, then supervised field trials.
- ISOBUS integration where compatible and licensed standards are available.
**Exit:** machine-specific validation and operational approval.

## Stage 8 — Harvest, market and orchestration
- Harvest lots, quality, storage, market intelligence and resource scheduling.
- Plan-vs-actual reconciliation and transparent economic metrics.
**Exit:** measured operational outcomes, not simulated claims.

Success metrics: provenance coverage, data completeness, spatial validity, ingest latency, availability, offline recovery, water/input per marketable yield, crop-model error, CV precision/recall, interventions, safety events, harvest losses and unit economics. Define baselines before setting target values.

Detailed plan and research: [docs/engineering/MASTER_PLAN_AND_RESEARCH.md](docs/engineering/MASTER_PLAN_AND_RESEARCH.md).
