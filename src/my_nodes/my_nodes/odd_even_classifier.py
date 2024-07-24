import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class OddEvenClassifier(Node):
    def __init__(self):
        super().__init__('odd_even_classifier')
        self.subscription = self.create_subscription(
            Int32,
            '/integers',
            self.listener_callback,
            10
        )
        self.publisher = self.create_publisher(String, '/oddeven', 10)

    def listener_callback(self, msg):
        number = msg.data
        result = 'even' if number % 2 == 0 else 'odd'
        result_msg = String()
        result_msg.data = result
        self.publisher.publish(result_msg)
        self.get_logger().info(f'Received integer: {number}, classified as: {result}')

def main(args=None):
    rclpy.init(args=args)
    node = OddEvenClassifier()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
