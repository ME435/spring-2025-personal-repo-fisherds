from mqtt_helper import MqttClient
from rosebot import RoseBot
import time

class App:
    def __init__(self):
        self.robot = RoseBot()
        
        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/fisherds/#",  # Could use me435/fisherds/to_pi
                                 publish_topic_name="me435/fisherds/to_computer",
                                 use_off_campus_broker=True)

    def mqtt_callback(self, type_name, payload):
        print(f"My callback: {type_name} - {payload}")
        
        if type_name == "set_speeds":
            self.robot.drive_system.set_speeds(payload[0], payload[1], payload[2], payload[3])
        if type_name == "stop":
            self.robot.drive_system.stop()
        

def main():
    print("Car MQTT Lab 5")
    app = App()
    
    try:
        while True:
            time.sleep(0.1)
            
            # Testing the wheel set_speeds method
            # app.mqtt_client.send_message("set_speeds", [-50, 50, 50, -50])
            # time.sleep(1.0)
            # app.mqtt_client.send_message("set_speeds", [50, -50, -50, 50])
            # time.sleep(1.0)
            # app.mqtt_client.send_message("stop")
            # time.sleep(2.0)
            
    except KeyboardInterrupt:
        print("Exiting...")
        app.robot.drive_system.stop()
        app.robot.drive_system.close()
        app.mqtt_client.close()

main()
