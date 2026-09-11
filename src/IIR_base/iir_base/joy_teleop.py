#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import joy
from geometry_msgs.msg import TwistedStamped

class ArcadeTeleop(Node):

    def __init__(self):
        super().__init__("arcade_teleop")

        self.linear_axis = 1
        self.angular_axis = 0

        self.max_linear_speed = 0.5
        self.max_angular_speed = 1.0
        self.deadzone = 0.05

        self.cmd_pub = self.create_publisher(
                TwistedStamped,
                "/diff_drive_controller/cmd_vel",
                10
        )

        self.joy_sub = self.create_subscription(
                Joy,
                "/joy",
                self.joy_callback,
                10
        )

    def apply_deadzone(self, value):
        if abs(value) < self.deadzone:
            return 0.0
        
        return value

    def joy_callback(self, msg):


        forward = self.apply_deadzone(msg.axes[1])
        turn    = self.apply_deadzone(msg.axes[0])

        cmd = TwistedStamped()
        cmd.header.stamp = self.get_clock().now().to_msg()

        if msg.button[5]:

            cmd.twist.linear.x = forward * self.max_linear_speed
            cmd.twist.angular.z = turn * self.max_angular_speed

        else:
            cmd.twist.linear.x = 0.0
            cmd.twist.angular.z = 0.0

        self.cmd_pub_publish(cmd)

def main(args=None):
    rclpy.init(args=args)

    node = ArcadeTeleop()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
