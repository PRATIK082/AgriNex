# AgriNex — Complete Project Blueprint

## 1. Product definition
An open-source Autonomous Agriculture Intelligence & Robotics Platform: a farm operating system joining field data, scientific agronomy, AI, robotics, drones, irrigation, crop lifecycle operations and production/market intelligence.

## 2. Vision and lifecycle
Survey land → characterize soil/water/terrain → choose crop/variety → prepare land → seed/plant → verify emergence → irrigate/drain → manage nutrients → scout/protect crop → monitor leaf/stem/root/flower/fruit/maturity → plan harvest → grade/store/transport → connect buyers → measure yield/quality/cost/impact → learn from verified outcomes.

Long-term minimal-human-intervention is bounded by a defined operating design domain. Autonomy levels per task/machine/crop: L0 manual; L1 advisory; L2 human-approved automation; L3 supervised autonomy; L4 bounded autonomy with independent safety and exception escalation; L5 aspirational end-to-end autonomy for a specified environment. Do not market the platform as fully autonomous globally.

## 3. Fifteen modules
| ID | Module | Scope |
|---|---|---|
| AGX-01 | Farm Digital Twin | Farm, field, boundary, zones, terrain, soil, water, assets and crop state |
| AGX-02 | Agricultural Data Intelligence | Weather, sensors, satellite, drone, machinery, yield and market ingestion/provenance |
| AGX-03 | AI Agronomist | Crop planning, calendars, evidence retrieval and reviewed decision support |
| AGX-04 | Soil Intelligence | Sampling, lab results, texture, pH, EC, organic matter, nutrients and water holding |
| AGX-05 | Land Preparation | Tillage, leveling, bed preparation, residue and implement planning |
| AGX-06 | Seeding & Planting | Seed/variety, rate, spacing, depth, row geometry and emergence |
| AGX-07 | Irrigation | ET, root-zone balance, valves, pumps, flow, pressure and drainage |
| AGX-08 | Nutrition/Fertigation | Nutrient budget, deficiency evidence, compatibility and supervised dosing |
| AGX-09 | Crop Protection | IPM, weed/pest/disease scouting and permitted treatment |
| AGX-10 | Aerial Robotics | Drone mapping, RGB/multispectral/thermal scouting and compliant adapters |
| AGX-11 | Ground Robotics | Tractor/implement, UGV, navigation, perception, fleet and maintenance |
| AGX-12 | Crop Health | Leaf, stem, root-zone, flower, fruit, biomass, stress and maturity |
| AGX-13 | Harvest/Post-Harvest | Readiness, picking integration, grading, storage, cold chain and losses |
| AGX-14 | Market Intelligence | Global/national production, supply/demand, mandi prices, trade and logistics |
| AGX-15 | Autonomy Orchestrator | Scheduling, authorization, dispatch, monitoring, verification and audit |

Shared services: identity/tenancy, audit, geospatial, units/time, provenance, offline sync, notifications, device registry, configuration, observability, localization and export.

## 4. Closed-loop operation
Observe → validate quality → estimate soil/crop state → run scientific models → recommend with evidence/uncertainty → check contraindications/regulations → obtain required approval → validate device/zone/weather/safety → dispatch bounded mission → execute locally → verify result → log cost/outcome → update digital twin. Reject stale/unsafe plans and notify on exceptions.

## 5. AI agents
Farm Planning; Crop Selection; Soil; Weather; Irrigation; Nutrition; Disease; Pest; Weed; Drone Mission; Robot Fleet; Crop Growth; Harvest; Market; Profit Optimization; Safety/Compliance; Farm Supervisor. Agents coordinate evidence/workflows; they do not replace scientific models or safety controllers.

## 6. Science and ML
Scientific: crop growth, ET, soil-water balance, nutrient budgets, disease epidemiology and IPM. ML: vision, forecasting, anomaly detection, yield estimation. Agents: evidence retrieval, explanation, workflow planning and approval routing. Candidates: AquaCrop, FAO-56, DSSAT, APSIM, PCSE, PyTorch, OpenCV, ONNX Runtime, scikit-learn and OR-Tools. Verify scope/license/calibration. LLMs must not invent pesticide doses/mixtures, fertilizer quantities or irrigation volumes.

## 7. Digital twin and data
Represent geometry/CRS, soil zones/samples, topography/drainage, irrigation network, crop/cultivar/stage, planting events, inputs, telemetry, observations, assets, operations, yield and quality. Use PostGIS for spatial entities, time-series storage for telemetry, object storage for imagery and Parquet/GeoParquet for analytics. Preserve source, observed/ingested time, timezone, units, calibration, quality, license/consent and processing lineage.

## 8. Market intelligence
Global production/trade → national/state/district supply → local arrivals/prices → weather/crop conditions → harvest overlap → storage/transport/buyer scenarios → farm margin and downside risk. Forecasts show freshness, horizon, intervals, model version, backtests and limitations. Revenue scenarios subtract seed, fertilizer, protection, water, energy, labor, machinery, finance, packaging, storage, transport, commission and losses. Forecasts are not guaranteed prices.

## 9. Hardware fleet
R01 tractor/implement; R02 precision seeder; R03 crop-care UGV; R04 harvesting robot; R05 scouting rover; D01 scouting drone; D02 compliant application-drone adapter; D03 mapping drone; D04 docking station; I01 irrigation/fertigation; S01 soil/weather/water nodes.

Candidates: Jetson-class edge compute or industrial PC; STM32/industrial PLC; RTK-GNSS, IMU, encoders, LiDAR/radar, RGB/stereo/depth, thermal/multispectral; CAN/CAN-FD/Ethernet; LoRaWAN/cellular/Wi-Fi; rated drives, valves, flow/pressure/tank sensors and BMS. Validate low-cost probes against lab methods.

## 10. Build vs buy
Buy/partner certified tractors, implements and drones in early pilots. Build orchestration, adapters, data pipeline, sensor/irrigation test rigs and low-speed non-spraying rover. Do not start with heavy autonomous tractor, pesticide aircraft or fruit-picking manipulator. Procurement requires operating-domain, payload, field geometry, traction, grade, crop row, obstacle, environment, power, safety, service, support and cost requirements.

## 11. Software stack
React/TypeScript; Python/FastAPI; PostgreSQL/PostGIS; TimescaleDB; MinIO/S3; GDAL/Rasterio/QGIS; PyTorch/OpenCV/ONNX; ROS 2/Nav2/Gazebo; MQTT; OR-Tools; MLflow; OpenTelemetry/Prometheus/Grafana; embedded C/C++/Rust. Modular monolith first; split services only with evidence. Keep safety loops local and deterministic.

## 12. Simulation
Virtual field/terrain; soil-water/crop growth; weather; robot dynamics/traction; sensors/localization/perception; irrigation; drone missions; fleet; market scenarios. Use Gazebo/ROS 2/Nav2, URDF/Xacro/SDF, crop model adapters and QGIS/GDAL/PostGIS. Test mud, slope, GNSS loss, occlusion, sensor/actuator faults, network outage, human/animal intrusion, blocked valves and low battery. Simulation alone is not safety proof.

## 13. Data sources
Global: FAOSTAT, USDA PSD/WASDE, AMIS, World Bank, UN Comtrade. India: AGMARKNET, data.gov.in, e-NAM, IMD, ICAR, Soil Health Card. Earth observation: Copernicus, NASA Earthdata, USGS, OpenStreetMap (ODbL obligations). Verify API, license, attribution, limits, coverage, freshness, units, CRS and terms.

## 14. Ecosystem research
Open source: farmOS, FarmBot, OpenDroneMap, QGIS, AgOpenGPS, Sowbot, Open-Weeding-Delta, OpenWeedLocator, OpenMower, ROS 2, Nav2, Gazebo, PCSE, DSSAT, APSIM, AquaCrop. Commercial: John Deere, Fendt, Case IH, AGCO, Monarch Tractor, AgroIntelli ROBOTTI, Carbon Robotics, Ecorobotix, Naio, FarmDroid, Niqo Robotics, DJI Agras, XAG, Garuda Aerospace, Marut Drones, IoTechWorld, CropX, Fasal, Netafim, Lindsay and Pessl/Metos. See [research catalogue](RESEARCH_CATALOG.md). These are discovery candidates, not audited endorsements.

## 15. Standards and regulation
Assess ISO 11783, ISO 18497 series (2024), ISO 25119, ISO 12100, ISO 13849, IEC 61508, ISO 13850, IEC 62443, ISO/IEC 27001, ISO 9001, ISO 14001 and ISO 22000. India: Drone Rules/current amendments, DGCA/eGCA/DigitalSky, agriculture drone SOPs, CIB&RC product registration/labels, state rules, water/environment/worker/food safety and privacy. Confirm editions/applicability with qualified experts; register is not legal advice.

## 16. Safety and security
Independent physical E-stop; local safety controller; safe state on communication/localization/sensor loss; geofence/exclusion zones; obstacle/person detection; watchdog; speed/force limits; manual isolation; spray interlocks/weather; operator authorization; audit; secure boot/signed OTA; least privilege; replay protection; incident/recovery procedures. Cloud AI must never bypass safety. Chemical application requires exact approved label, operator qualifications, equipment compatibility, drift/buffer/weather controls and permissions.

## 17. V-model validation
Requirements → architecture → detailed design → implementation → code review/static analysis → unit → integration → system → simulation → HIL → controlled field validation → release evidence. Link requirements to design/code/tests/results. CV: per-class precision/recall, calibration and domain shift. Robotics: localization error, stopping distance, collisions/near misses, intervention, task success, uptime and recovery. Agronomy: local ground truth, farm/season-separated evaluation and expert review.

## 18. Pilot
Small experimental plot and one crop chosen by research: farm map; soil moisture/temp/pH/EC (lab validation); weather; RGB imagery; drone imagery ingestion; plant-health model; irrigation recommendation; drip test rig; supervised nutrition plan; low-speed rover; dashboard/digital twin; water/input/growth/cost/yield tracking. Prove detect → decide → authorize → execute → verify.

## 19. Business hypotheses
Farm SaaS; drone-as-a-service; robot-as-a-service; shared equipment/FPO fleet; input procurement; produce buyer/processor marketplace; lawful aggregated data; insurance/credit partnerships. Validate willingness to pay and total cost of ownership.

## 20. Licensing
Proposed core software Apache-2.0; hardware evaluate CERN-OHL-S/W per design; docs CC BY 4.0 where suitable; datasets/model weights separately licensed after rights review. Preserve upstream licenses/notices. Software licensing does not grant rights to images, crop datasets, protocols, patents or model weights.
