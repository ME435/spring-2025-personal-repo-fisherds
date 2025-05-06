from rosebot import RoseBot
from mqtt_helper import MqttClient
import time

class App:
    def __init__(self):
        self.robot = RoseBot()
        
        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/fisherds/#",  # Could also use "me435/fisherds/to_pi"
                                 publish_topic_name="me435/fisherds/to_computer",
                                 mqtt_broker_ip_address="broker.hivemq.com",
                                 use_off_campus_broker=True)        
        
    def mqtt_callback(self, type_name, payload):
        print(f"My Callback: {type_name} - {payload}")
        
        if type_name == "set_speeds":
            self.robot.drive_system.set_speeds(payload[0], payload[1], payload[2], payload[3])

        if type_name == "stop":
            self.robot.drive_system.stop()
        
        if type_name == "pan":
            self.robot.servo_head.set_pan_position(payload)
        if type_name == "tilt":
            self.robot.servo_head.set_tilt_position(payload)
            
        if type_name == "beep":
            self.robot.buzzer.beep(on_time=0.1, off_time=0.3, n=2)

def main():
    print("Car MQTT for Lab 5")
    app = App()
    
    try:
        while True:
            time.sleep(0.1)
            
            # Localhost testing for wheel speeds
            # app.mqtt_client.send_message("set_speeds", [-50, 50, 50, -50])    # Pretend left arrow press
            # time.sleep(1)
            # app.mqtt_client.send_message("set_speeds", [50, -50, -50, 50])    # Pretend right arrow press
            # time.sleep(1)
            # app.mqtt_client.send_message("stop")    # Pretend key release
            # time.sleep(2)
            
            # Test the servo head
            # app.mqtt_client.send_message("pan", 90)
            # app.mqtt_client.send_message("tilt", 90)
            # time.sleep(2)
            # app.mqtt_client.send_message("pan", 20)
            # time.sleep(2)
            # app.mqtt_client.send_message("pan", 160)
            # time.sleep(2)
            # app.mqtt_client.send_message("pan", 90)
            # time.sleep(2)
            # app.mqtt_client.send_message("tilt", 70)
            # time.sleep(2)
            # app.mqtt_client.send_message("tilt", 160)
            # time.sleep(2)
            # app.mqtt_client.send_message("pan", 90)
            # app.mqtt_client.send_message("tilt", 90)
            # time.sleep(4)

    except KeyboardInterrupt:
        print("Exiting...")
        app.robot.servo_head.reset()
        app.robot.drive_system.stop()
        app.robot.drive_system.close()
        app.mqtt_client.close()  
          
main()

