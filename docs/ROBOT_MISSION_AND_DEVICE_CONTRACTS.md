# Robot Mission and Device Contracts
Mission envelope: mission_id; tenant/farm/field/zone; device/capability; operation; geometry/waypoints; operating window; preconditions; speed/force/flow/depth limits; duration; source recommendation; approvals; expiry; idempotency key; safety profile; abort criteria; trace ID.

Desired state ≠ command ≠ acknowledgement ≠ measured state ≠ verified outcome. Store separately with timestamps/device identity.

Device capability profile: vendor/model/firmware; operations; payload/tool; operating envelope; coordinate frames; telemetry/command schema; calibration; maintenance; safety functions; offline behavior; protocol; conformance tests.

Commands must be authenticated, signed where feasible, time-limited, replay-resistant, sequenced, authorized and checked on device/edge for range/geofence. Define faults: localization degraded, obstacle, implement jam, actuator mismatch, low battery, temperature, network loss, boundary violation, stale sensor. Map each to pause/stop/abort/notify/recovery via risk analysis.

Use ROS 2 actions/services for robot tasks and MQTT/HTTPS for telemetry/control plane as appropriate. Version JSON Schema/OpenAPI/Protobuf. MQTT delivery does not prove physical execution.
