import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class KeyboardControl(Node):
    def __init__(self):
        super().__init__('keyboard_control')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        key = input("Enter direction (w/a/s/d for linear and q/e for angular): ").strip().lower()
        if key == 'w':
            msg.linear.x = 0.2
        elif key == 's':
            msg.linear.x = -0.2
        elif key == 'a':
            msg.linear.y = 0.2
        elif key == 'd':
            msg.linear.y = -0.2
        elif key == 'q':
            msg.angular.z = 0.2
        elif key == 'e':
            msg.angular.z = -0.2
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

