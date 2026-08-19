#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import JointState
from std_msgs.msg import String

from math import radians


class JointFeedbackNode(Node):

    def __init__(self):

        super().__init__('joint_feedback_node')

        # ==========================================
        # Subscribe to Arduino Feedback
        # ==========================================

        self.subscription = self.create_subscription(
            String,
            '/joint_feedback',
            self.feedback_callback,
            10
        )

        # ==========================================
        # Publish Joint States
        # ==========================================

        self.joint_state_publisher = self.create_publisher(
            JointState,
            '/joint_states',
            10
        )

        self.get_logger().info(
            'Joint Feedback Node Started'
        )

    # ==============================================
    # Callback
    # ==============================================

    def feedback_callback(self, msg):

        try:

            # Example:
            # "10,20,30,40"

            angles = msg.data.split(',')

            if len(angles) != 4:

                self.get_logger().warn(
                    'Invalid joint data received'
                )

                return

            # Convert Degrees to Radians

            joint_2 = radians(float(angles[0]))
            joint_3 = radians(float(angles[1]))
            joint_4 = radians(float(angles[2]))
            joint_5 = radians(float(angles[3]))

            # ======================================
            # Create JointState Message
            # ======================================

            joint_state = JointState()

            joint_state.header.stamp = \
                self.get_clock().now().to_msg()

            joint_state.name = [
                'joint_2',
                'joint_3',
                'joint_4',
                'joint_5'
            ]

            joint_state.position = [
                joint_2,
                joint_3,
                joint_4,
                joint_5
            ]

            # ======================================
            # Publish Joint States
            # ======================================

            self.joint_state_publisher.publish(
                joint_state
            )

            self.get_logger().info(
                f'Updated Joints: {msg.data}'
            )

        except Exception as e:

            self.get_logger().error(
                f'Error: {e}'
            )


def main(args=None):

    rclpy.init(args=args)

    node = JointFeedbackNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
