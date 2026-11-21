# Architecture and Software Design
![Architecture](assets/agrinex-architecture.svg)

## Layered architecture
1. Experience: web, mobile, voice/local language and operator console.
2. Domain: farm, crop cycle, agronomy, soil, irrigation, protection, harvest and market.
3. Intelligence: scientific models, ML, decision support and optimization.
4. Data fabric: geospatial, time series, imagery, provenance and external sources.
5. Autonomy: mission lifecycle, scheduler, authorization, fleet and verification.
6. Edge/device: gateway, sensors, PLC/MCU, ROS 2 robots, drones and equipment adapters.
7. Independent safety: E-stop, safety controller, interlocks, watchdogs and manual isolation.

## Main feedback loop
Observe → validate → estimate state → recommend → risk-check/simulate → authorize → dispatch → execute locally → verify → audit → learn.

## Technology choices
React/TypeScript; Python/FastAPI; PostgreSQL/PostGIS; TimescaleDB; MinIO/S3; GDAL/Rasterio/QGIS; PyTorch/OpenCV/ONNX; ROS 2/Nav2/Gazebo; MQTT; OR-Tools; MLflow; OpenTelemetry/Prometheus/Grafana; embedded C/C++/Rust.

## Architectural rules
- Modular monolith first; service extraction only with evidence.
- Versioned APIs/events and explicit units/CRS/time.
- Commands are authenticated, authorized, bounded, time-limited, idempotent and audited.
- Desired state, command, acknowledgement, measured state and verified outcome are distinct.
- Local control remains functional during cloud/network outage.
- Agents can propose and request approvals; never directly control safety-critical actuators.
- Data providers and OEMs are replaceable adapters.
- Farm data must be exportable and governed with transparent rights.

## Deployment
Cloud: multi-farm management, analytics, model training and market feeds. Farm edge: offline cache, gateway, local inference and operator interface. Machine edge: real-time control, perception and localization. Safety hardware is independent of cloud/LLM.

## Diagrams
See [system context](architecture/diagrams/SYSTEM_CONTEXT.mmd) and [mission lifecycle](architecture/diagrams/MISSION_LIFECYCLE.mmd).
