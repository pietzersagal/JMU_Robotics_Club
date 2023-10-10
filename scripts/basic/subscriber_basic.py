import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Subscriber(Node):
    
    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.subscriber_callback, 10)
        
    def subscriber_callback(self, msg):
        self.get_logger().info("Moved X: %d" % msg.linear.x)
        
def main(args=None):
    rclpy.init(args=args)
    subscriber = Subscriber()
    rclpy.spin(subscriber)
    publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
