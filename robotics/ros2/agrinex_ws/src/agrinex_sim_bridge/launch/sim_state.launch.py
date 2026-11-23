from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([Node(package="agrinex_sim_bridge",executable="farm_state_publisher",name="farm_state_publisher",output="screen")])
