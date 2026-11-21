# Robotics and Hardware Engineering

## Fleet
| ID | Platform | Operations |
|---|---|---|
| AGX-R01 | Tractor/implement | Tillage, bed prep, transport |
| AGX-R02 | Precision seeder | Metering, spacing, depth, emergence |
| AGX-R03 | Crop-care UGV | Scouting, mechanical weeding, selective care |
| AGX-R04 | Harvest robot | Fruit detection, maturity, picking, grading |
| AGX-R05 | Scouting rover | Plant imagery, pest and environment inspection |
| AGX-D01 | Scouting drone | RGB/multispectral/thermal |
| AGX-D02 | Application drone adapter | Approved supervised missions |
| AGX-D03 | Mapping drone | Terrain and photogrammetry |
| AGX-D04 | Dock | Charging and readiness |
| AGX-I01 | Irrigation controller | Valves, pumps, flow, pressure, fertigation |

## Components
Jetson-class/industrial edge compute; STM32/industrial PLC for deterministic IO; RTK-GNSS, IMU, encoders, LiDAR/radar; RGB/stereo/depth, thermal and multispectral; rated drives; CAN/CAN-FD/Ethernet; LoRaWAN/cellular/Wi-Fi; battery/BMS; soil moisture/temp, calibrated soil sampling, weather, flow/pressure/tank sensors. ESP32 is for non-safety prototypes only. Low-cost soil probes need lab validation.

## ROS 2
Drivers; robot_state_publisher; localization; perception; obstacle layers; Nav2 planner/controller; mission executor; implement controller; diagnostics; telemetry; independent safety interface.

## Build vs buy
Buy/partner certified tractors, implements and drones. Build adapters, sensor/irrigation rigs and a low-speed non-spraying scouting rover. Begin seeder with stationary test fixture. Harvest manipulation is advanced R&D.

## Procurement gate
Define operating domain, payload, dimensions, row spacing, terrain/grade, traction, obstacles, environmental rating, duty cycle, localization, power, service, local support, cost, hazard analysis and compliance before purchase.
