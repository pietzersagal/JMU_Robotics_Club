import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class Subscriber(Node):
    
    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(String, 'customtopic', self.subscriber_callback, 10)
        
    def subscriber_callback(self, msg):
        #if(msg.linear.x != 0.0)
        self.get_logger().info("%s" % str(msg.data))
        
def main(args=None):
    rclpy.init(args=args)
    subscriber = Subscriber()
    rclpy.spin(subscriber)
    publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
