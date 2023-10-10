import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):
    
    def __init__(self):
        super().__init__('publisher')
        self.publisher = self.create_publisher(String, 'customtopic', 10)
        timer_period = 0.03
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    def timer_callback(self):
        msg = String()
        msg.data = "Test"
        self.publisher.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
