import mqtt_helper as mh
import time
import gpiozero as gz
import datetime
import rosebot

class App:

    def __init__(self):
        print("Using MQTT with a class")

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/fisherds/#",
                            publish_topic_name="me435/fisherds/to_computer",
                            use_off_campus_broker=False)
        self.mqtt_client.callback = self.mqtt_callback

        self.robot = rosebot.RoseBot()
        self.is_streaming = False
        self.drive_until_wall = False
        self.drive_until_line = False
        self.is_line_following = False


    def mqtt_callback(self, message_type, payload):
        print("Received type:", message_type)
        print("Received payload:", payload)
        
        if message_type == "is_streaming":
            self.is_streaming = payload
        
        if message_type == "is_line_following":
            self.is_line_following = payload
            
        if message_type == "set_speeds":
            self.robot.drive_system.set_speeds(payload[0], payload[1], payload[2], payload[3])
            
        if message_type == "stop":
            self.robot.drive_system.stop()
            
        if message_type == "left":
            self.robot.drive_system.spin_in_place_for_degrees(payload, 40, True)
        if message_type == "right":
            self.robot.drive_system.spin_in_place_for_degrees(payload, 40, False)
            
        if message_type == "pan":
            self.robot.servo_head.set_pan_position(payload)
        if message_type == "tilt":
            self.robot.servo_head.set_tilt_position(payload)
            
        if message_type == "beep":
            self.robot.buzzer.beep(on_time=0.1, off_time=0.3, n=2)
            
        if message_type == "set_led":
            self.robot.leds.set_led(payload[0], payload[1], payload[2], payload[3])
        if message_type == "set_all_leds":
            self.robot.leds.set_all_leds(payload[0], payload[1], payload[2])    
            
        if message_type == "mode":
            if payload == "drive_until_wall":
                self.drive_until_wall = True
                self.robot.drive_system.go(90, 90)   
            if payload == "drive_until_line":
                self.drive_until_line = True
                self.robot.drive_system.go(90, 90)
        
        if message_type == "get_voltage":
            voltage = self.robot.adc.get_battery_voltage()
            self.mqtt_client.send_message("voltage", voltage)

                
def main():
    print("MQTT Car")
    app = App()

    last_time_sent_s = 0
    
    # Purely as a talking to myself test, turn on sensor streaming
    # time.sleep(0.5)  # allow mqtt to connect
    # app.mqtt_client.send_message("is_streaming", True)
    
    try:
        while True:
            time.sleep(0.1)
            
            # print("Test Beep")
            # app.mqtt_client.send_message("beep")
            # time.sleep(5)
            
            # print("Test set_speeds")
            # app.mqtt_client.send_message("set_speeds", [40, 40, 0, 0])
            # time.sleep(1)
            # app.mqtt_client.send_message("set_speeds", [0, 0, 0, 0])
            # time.sleep(5)
            
            # print("Test set_led and set_all_leds")
            # app.mqtt_client.send_message("set_led", [0, 255, 0, 0])
            # time.sleep(1)
            # app.mqtt_client.send_message("set_led", [1, 0, 255, 0])
            # time.sleep(1)
            # app.mqtt_client.send_message("set_led", [7, 0, 0, 255])
            # time.sleep(1)
            # app.mqtt_client.send_message("set_all_leds", [0, 255, 255])
            # time.sleep(1)
            # app.mqtt_client.send_message("set_all_leds", [0, 0, 0])
            # time.sleep(1)
            
            
            
            if app.drive_until_wall:
                if app.robot.ultrasonic.get_distance() < 0.2:
                    app.robot.drive_system.stop()
                    app.drive_until_wall = False
            
            now = datetime.datetime.now() # current date and time
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            timestamp_s = now.timestamp()
            if timestamp_s - last_time_sent_s > 2 and app.is_streaming:
                last_time_sent_s = timestamp_s
                app.mqtt_client.send_message("line_sensor_reading", 
                                            {"timestamp": date_time,
                                            "left": app.robot.line_sensors.get_left(),
                                            "middle": app.robot.line_sensors.get_middle(),
                                            "right": app.robot.line_sensors.get_right()})
    except KeyboardInterrupt:
        print("Exiting...")
        app.robot.drive_system.stop()
        app.robot.buzzer.beep(on_time=0.1, off_time=0.3, n=2)
        app.robot.servo_head.reset()
        time.sleep(0.5)
        app.robot.leds.turn_off()




main()