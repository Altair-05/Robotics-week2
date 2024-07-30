import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
import math

class MoveToGoal(Node):
    def __init__(self):
        super().__init__('move_to_goal')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            Odometry,
            'odom',
            self.odom_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.goal_x = 2.0  # Set your goal x-coordinate
        self.goal_tolerance = 0.1  # Set tolerance for reaching the goal

    def odom_callback(self, msg):
        # Get current position from Odometry
        position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation
        _, _, yaw = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
        distance = math.sqrt((self.goal_x - position.x)**2)

        if distance > self.goal_tolerance:
            msg = Twist()
            msg.linear.x = 0.2  # Set linear velocity
            msg.angular.z = 0.0  # No angular velocity
            self.publisher_.publish(msg)
        else:
            msg = Twist()
            msg.linear.x = 0.0  # Stop the robot
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info('Goal reached')

def main(args=None):
    rclpy.init(args=args)
    node = MoveToGoal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

