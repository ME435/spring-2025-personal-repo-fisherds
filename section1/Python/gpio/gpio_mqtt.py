import gpiozero as gz
from mqtt_helper import MqttClient
import time

class App:
    def __init__(self):
        self.led_board = gz.LEDBoard(red=14, yellow=15, green=18, pwm=True)
        
        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/fisherds/#",
                                 publish_topic_name="me435/fisherds/to_computer",
                                 use_off_campus_broker=False)

    def mqtt_callback(self, type_name, payload):
        print(f"My Callback: {type_name} - {payload}")
        if type_name == "red":
            if payload == "on":
                self.led_board.red.on()
            elif payload == "off":
                self.led_board.red.off()

def main():
    print("GPIO MQTT Test")
    app = App()
    
    try:
        while True:
            time.sleep(0.1)
            # app.mqtt_client.send_message("red", "on")    
            # time.sleep(2)
            # app.mqtt_client.send_message("red", "off")    
            # time.sleep(2)
            
    except KeyboardInterrupt:
        print("Exiting...")
        app.mqtt_client.close()  
          
main()

