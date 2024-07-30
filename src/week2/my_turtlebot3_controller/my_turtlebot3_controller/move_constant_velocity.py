import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveConstantVelocity(Node):
    def __init__(self):
        super().__init__('move_constant_velocity')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.2  # Set the linear velocity
        msg.angular.z = 0.0  # Ensure angular velocity is zero for straight movement
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg}')  # Log the message being published

def main(args=None):
    rclpy.init(args=args)
    node = MoveConstantVelocity()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

