# Test Strategy
Test pyramid/V-model: static checks → unit → component → contract → integration → system → simulation → HIL → supervised field validation. Map tests to requirement IDs and risks.

Fixtures: agronomy lab results and controlled plots; GIS boundaries/CRS/invalid polygons; sensor calibration/drift/dropout/time skew; robotics GNSS loss/slip/obstacles/actuator/E-stop; irrigation stuck valve/pressure/leak/power; AI poor-quality/OOD images and abstention; market missing/revised/delayed data; security unauthorized device/replay/stale command/OTA rollback.

Evidence record: test ID, requirement IDs, build/model version, hardware revision, dataset license/version, environment, procedure, expected/actual, logs, reviewer and anomalies.

Release gate: no unresolved critical safety/security defects; approvals; passing tests; known limitations; calibrated hardware; operator training/recovery procedure; legal approvals for field use.
