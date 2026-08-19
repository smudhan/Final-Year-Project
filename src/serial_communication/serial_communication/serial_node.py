import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import serial
import threading


class SerialCommunicationNode(Node):

    def __init__(self):

        super().__init__('serial_communication_node')

        # Serial Port
        self.port = 'COM10'
        self.baud_rate = 115200

        # Open Serial
        try:

            self.serial_port = serial.Serial(
                self.port,
                self.baud_rate,
                timeout=1
            )

            self.get_logger().info(
                f'Serial Connected on {self.port}'
            )

        except Exception as e:

            self.get_logger().error(
                f'Failed to connect serial port: {e}'
            )

            return

        # Subscriber
        self.subscription = self.create_subscription(
            String,
            '/joint_angles',
            self.joint_angle_callback,
            10
        )

        # Publisher
        self.feedback_publisher = self.create_publisher(
            String,
            '/joint_feedback',
            10
        )

        # Serial Thread
        self.serial_thread = threading.Thread(
            target=self.read_serial_data
        )

        self.serial_thread.daemon = True
        self.serial_thread.start()

        self.get_logger().info(
            'ROS2 Serial Communication Node Started'
        )

    def joint_angle_callback(self, msg):

        try:

            data = msg.data

            serial_data = data + '\n'

            self.serial_port.write(
                serial_data.encode()
            )

            self.get_logger().info(
                f'Sent to Arduino: {data}'
            )

        except Exception as e:

            self.get_logger().error(
                f'Serial Write Error: {e}'
            )

    def read_serial_data(self):

        while rclpy.ok():

            try:

                if self.serial_port.in_waiting > 0:

                    incoming_data = self.serial_port.readline() \
                        .decode('utf-8') \
                        .strip()

                    feedback_msg = String()

                    feedback_msg.data = incoming_data

                    self.feedback_publisher.publish(
                        feedback_msg
                    )

                    self.get_logger().info(
                        f'Published Feedback: {incoming_data}'
                    )

            except Exception as e:

                self.get_logger().error(
                    f'Serial Read Error: {e}'
                )

    def destroy_node(self):

        try:
            self.serial_port.close()

        except:
            pass

        super().destroy_node()


def main(args=None):

    rclpy.init(args=args)

    node = SerialCommunicationNode()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:

        node.get_logger().info(
            'Node Stopped'
        )

    finally:

        node.destroy_node()

        rclpy.shutdown()


if __name__ == '__main__':
    main()
