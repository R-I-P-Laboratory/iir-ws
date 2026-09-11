from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    joy_teleop_node = Node(
        package='IIR_base',
        executable='joy_teleop.py',
        name='joy_teleop',
        output='screen',
    )

    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        output='screen',
    )

    return LaunchDescription([
        joy_node,
        joy_teleop_node,
    ])
