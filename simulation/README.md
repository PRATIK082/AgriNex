# Simulation Foundation
Gazebo world: gazebo/worlds/agrinex_demo_farm.sdf. ROS package: ../robotics/ros2/agrinex_ws.

In ROS 2 Jazzy: source /opt/ros/jazzy/setup.bash; cd robotics/ros2/agrinex_ws; colcon build --symlink-install; source install/setup.bash; ros2 launch agrinex_sim_bridge sim_state.launch.py; ros2 topic echo /agrinex/sim/farm_state. Synthetic only; no real robot integration or safety validation.
