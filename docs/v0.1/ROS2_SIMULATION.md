# ROS 2 and Simulation Foundation
Workspace: robotics/ros2/agrinex_ws/src/agrinex_sim_bridge. Gazebo scene: simulation/gazebo/worlds/agrinex_demo_farm.sdf. Target environment to validate: ROS 2 Jazzy on Ubuntu 24.04 with compatible Gazebo Harmonic.

Topology: Gazebo world/sensors → ROS 2 topics/actions → edge adapter → secure AgriNex gateway. Prefer standard ROS messages; create custom interfaces only after contracts stabilize. Define frames, timestamps, QoS, lifecycle, robot namespaces and fault states. Pin exact ROS/Gazebo dependencies after environment CI validation.

Build: source /opt/ros/jazzy/setup.bash; cd robotics/ros2/agrinex_ws; colcon build --symlink-install; source install/setup.bash; ros2 launch agrinex_sim_bridge sim_state.launch.py; ros2 topic echo /agrinex/sim/farm_state. Publisher is synthetic. Simulation is not safety certification; no real robot connection is provided.
