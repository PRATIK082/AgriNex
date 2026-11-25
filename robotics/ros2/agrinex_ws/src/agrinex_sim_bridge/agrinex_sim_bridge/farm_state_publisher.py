import json
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class FarmStatePublisher(Node):
    def __init__(self):
        super().__init__("agrinex_farm_state_publisher")
        self.pub=self.create_publisher(String,"/agrinex/sim/farm_state",10)
        self.seq=0
        self.timer=self.create_timer(1.0,self.publish_state)
    def publish_state(self):
        self.seq+=1
        msg=String()
        msg.data=json.dumps({"schema_version":"1.0","simulation":True,"sequence":self.seq,"farm_id":"demo-farm","state":"nominal","note":"Synthetic data only; not real device state."})
        self.pub.publish(msg)
def main(args=None):
    rclpy.init(args=args); node=FarmStatePublisher()
    try: rclpy.spin(node)
    except KeyboardInterrupt: pass
    finally: node.destroy_node(); rclpy.shutdown()
