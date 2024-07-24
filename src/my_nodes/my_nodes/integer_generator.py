import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class IntegerGenerator(Node):
    def __init__(self):
        super().__init__('integer_generator')
        self.publisher = self.create_publisher(Int32, '/integers', 10)
        self.timer = self.create_timer(2.0, self.publish_integer)  

    def publish_integer(self):
        msg = Int32()
        msg.data = random.randint(0, 1000)  
        self.publisher.publish(msg)
        self.get_logger().info(f'Published integer: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = IntegerGenerator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
