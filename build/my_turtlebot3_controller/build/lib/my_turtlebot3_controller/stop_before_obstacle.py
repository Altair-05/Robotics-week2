import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class StopBeforeObstacle(Node):
    def __init__(self):
        super().__init__('stop_before_obstacle')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(LaserScan, 'scan', self.scan_callback, 10)
        self.stop_distance = 0.1
        self.obstacle_distance = float('inf')

    def scan_callback(self, msg):
        self.obstacle_distance = min(msg.ranges)

    def timer_callback(self):
        if self.obstacle_distance < self.stop_distance:
            msg = Twist()
            msg.linear.x = 0.0
            self.publisher_.publish(msg)
        else:
            msg = Twist()
            msg.linear.x = 0.2
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = StopBeforeObstacle()
    node.create_timer(0.1, node.timer_callback)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

