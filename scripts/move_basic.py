import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Publisher(Node):
    
    def __init__(self):
        super().__init__('publisher')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.03
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    def timer_callback(self):
        move = Twist()
        ######EDIT FOR MOVEMENT ###########
        move.linear.x = 0.0
        move.angular.z = 0.0
        #########################################
        self.publisher.publish(move)
        self.get_logger().info("Moving bot: %d" % self.i)
        self.i += 1
        
def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
