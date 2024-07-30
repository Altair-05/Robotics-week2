import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class MoveToGoal(Node):
    def __init__(self):
        super().__init__('move_to_goal')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(Odometry, 'odom', self.odom_callback, 10)
        self.goal_x = 2.0
        self.goal_tolerance = 0.1
        self.current_position = None

    def odom_callback(self, msg):
        self.current_position = msg.pose.pose.position

    def timer_callback(self):
        if self.current_position is None:
            return

        distance_to_goal = abs(self.goal_x - self.current_position.x)
        if distance_to_goal > self.goal_tolerance:
            msg = Twist()
            msg.linear.x = 0.2
            self.publisher_.publish(msg)
        else:
            msg = Twist()
            msg.linear.x = 0.0
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MoveToGoal()
    node.create_timer(0.1, node.timer_callback)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

