# Robotics and Hardware Engineering Plan

## Robot families
| ID | Platform | Operations |
|---|---|---|
| AGX-R01 | Tractor/implement integration | Tillage, bed prep, transport and implements |
| AGX-R02 | Precision seeder | Metering, spacing, depth, row alignment, emergence |
| AGX-R03 | Crop-care UGV | Scouting, mechanical weeding and selective care |
| AGX-R04 | Harvest robot | Fruit detection, maturity, picking, handling and grading |
| AGX-R05 | Scouting rover | Plant-level imagery, pest and soil/environment inspection |
| AGX-D01 | Scouting drone | RGB/multispectral/thermal crop monitoring |
| AGX-D02 | Application drone adapter | Approved, compliant application missions |
| AGX-D03 | Mapping drone | Terrain, photogrammetry and 3D maps |
| AGX-D04 | Docking station | Charging, battery and mission readiness |
| AGX-I01 | Irrigation controller | Valves, pumps, flow, pressure and fertigation |

## Components
Edge compute: Jetson-class or industrial x86/ARM. MCU/PLC: STM32/industrial PLC for deterministic IO; ESP32 for non-safety prototypes only. Navigation: RTK-GNSS, IMU, wheel encoders, visual odometry, LiDAR/radar. Perception: RGB/stereo/depth, thermal and multispectral. Drives: rated BLDC/servo, CAN/CAN-FD. Field connectivity: LoRaWAN, cellular, Wi-Fi, Ethernet. Power: correctly sized battery/BMS, charging and isolation. Sensors: moisture/temp, calibrated soil sampling, weather, flow, pressure, tank level and water quality.

## ROS 2 stack
Hardware drivers; robot_state_publisher; localization; perception; obstacle layers; Nav2 planner/controller; mission executor; implement controller; diagnostics; telemetry bridge; independent safety interface.

## Drone software
Mission planning, geofencing, flight telemetry, battery health, image capture, orthomosaic generation, field-zone analytics and task reporting. Start by ingesting imagery from an existing legally operated aircraft; do not design a spray drone first.

## Build vs buy
Buy/partner certified tractors, implements and drones. Build adapters, sensor/irrigation rigs and a low-speed non-spraying scouting rover. Seeder metering should begin as a stationary test fixture. Harvest robotics is advanced R&D.

## Procurement requirements
Operating design domain, payload, dimensions, row spacing, terrain/grade, soil traction, obstacle set, IP/environmental rating, duty cycle, localization availability, power, service, local support, cost, hazard analysis and compliance path.

## Simulation and tests
ROS 2 + Gazebo, URDF/Xacro/SDF, Nav2, robot_localization. Test mud, slope, crop-row variation, GNSS loss, sensor occlusion, wheel slip, people/animals, low battery, network loss, actuator/implement faults and safe recovery. Simulation is not safety certification.
