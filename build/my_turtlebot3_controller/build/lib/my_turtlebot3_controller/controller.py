import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleBot3Controller(Node):
    def __init__(self):
        super().__init__('turtlebot3_controller')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('TurtleBot3Controller node has been started.')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.2
        msg.angular.z = 0.1
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)

def main(args=None):
    rclpy.init(args=args)
    turtlebot3_controller = TurtleBot3Controller()
    rclpy.spin(turtlebot3_controller)
    turtlebot3_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

