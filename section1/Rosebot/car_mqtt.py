from rosebot import RoseBot
from mqtt_helper import MqttClient
import time
from datetime import datetime

class App:
    def __init__(self):
        self.robot = RoseBot()
        self.is_sensor_streaming = False
        self.mode = "none"
        
        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/fisherds/#",  # Could also use "me435/fisherds/to_pi"
                                 publish_topic_name="me435/fisherds/to_computer",
                                 use_off_campus_broker=False)        
        
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
        
        if type_name == "is_streaming":
            self.is_sensor_streaming = payload

        if type_name == "mode":
            self.mode = payload
            

def main():
    print("Car MQTT for Lab 5")
    app = App()
    
    try:
        last_time_sent = 0
        while True:
            time.sleep(0.1)
            
            if app.is_sensor_streaming:
                now = datetime.now()
                timestamp_s = now.timestamp()
                if timestamp_s - last_time_sent > 2.0:
                    last_time_sent = timestamp_s
                    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                    print("date and time:", date_time)	
                    app.mqtt_client.send_message("line_sensor_reading", {"timestamp": date_time,
                                                                         "left": app.robot.line_sensors.get_left(),
                                                                         "middle": app.robot.line_sensors.get_middle(),
                                                                         "right": app.robot.line_sensors.get_right()})            
            if app.mode == "line_following":
                print("TODO: run 1 lap of my line following program. With NO delay.")
                time.sleep(1)  # TODO: remove, reduces printing for now
            elif app.mode == "light_following":
                print("TODO: Get the photoresistor values and adjust the speeds.")
                time.sleep(1)  # TODO: remove, reduces printing for now
            elif app.mode == "drive_until_wall":
                if app.robot.ultrasonic.get_cm() < 20:
                    app.robot.drive_system.stop()
                    app.robot.buzzer.beep(on_time=0.1, off_time=0.3, n=2)
                    app.mode = "none"
            elif app.mode == "drive_until_line":
                if app.robot.line_sensors.get_lineword() != "WWW":
                    app.robot.drive_system.stop()
                    app.robot.buzzer.beep(on_time=0.1, off_time=0.3, n=2)
                    app.mode = "none"
                    
            
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

