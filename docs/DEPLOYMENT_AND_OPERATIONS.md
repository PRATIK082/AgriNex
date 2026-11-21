# Deployment and Operations
Environments: local development, CI, simulation, hardware bench/HIL, supervised pilot, production. Separate credentials and datasets.

Farm edge caches bounded offline work and telemetry. Critical control/safety remain local. Cloud outage must not disable E-stop or local safe-state logic. Define sync conflict policy and command expiry.

Device lifecycle: provision identity → register capabilities → calibrate → approve firmware → stage signed update → health check → gradual deploy → monitor → rollback if needed → decommission/revoke identity.

Correlate logs/metrics/traces with farm/field/device/mission IDs without leaking sensitive data. Monitor sensor freshness, model drift, mission success, intervention, safety events, network and battery health.

Back up transactional data/configuration and test restores. Define RPO/RTO per service. Maintain manual operating procedures. Version software, firmware, schemas and models independently; publish release notes, SBOM, known issues, migration, signed artifacts and evidence. No silent updates to field machines.
