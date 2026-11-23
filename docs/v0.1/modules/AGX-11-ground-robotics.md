# AGX-11 — Ground Robotics

## Purpose
Integrate UGV/tractor autonomy through capabilities, localization, missions and telemetry.

## Functional requirements
- AGX-11-FR-001: Register platform/tool/firmware/frames/sensors/calibration/safety
- AGX-11-FR-002: map/localization/geofence/obstacles
- AGX-11-FR-003: validate terrain/slope/row/payload
- AGX-11-FR-004: authorized expiring idempotent missions
- AGX-11-FR-005: monitor pose/velocity/battery/actuator/obstacles
- AGX-11-FR-006: safe state on localization/watchdog/comms/fault
- AGX-11-FR-007: separate action/command/ack/telemetry/outcome
- AGX-11-FR-008: manual takeover/E-stop/recovery.

## Data ownership and interfaces
Own DeviceCapability, RobotMission, RobotTelemetry, MissionOutcome; consumes AGX-01/02/15.

## Acceptance, safety and security
ROS/Gazebo fault injection. No real actuation before safety case, HIL and supervised field validation.
