from mqtt_helper import MqttClient
import gpiozero as gz
import time

class App:
    def __init__(self):
        self.red_led = gz.LED(14)
        
        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/fisherds/#",
                                 publish_topic_name="me435/fisherds/to_computer",
                                 use_off_campus_broker=False)

    def mqtt_callback(self, type_name, payload):
        print(f"My callback: {type_name} - {payload}")
        if type_name == "red":
            if payload == "on":
                self.red_led.on()
            elif payload == "off":
                self.red_led.off()
            else:
                print(f"Unknown payload: {payload}")


def main():
    print("GPIO MQTT Example")
    app = App()
    
    try:
        while True:
            time.sleep(0.1)
            # app.mqtt_client.send_message("red", "on")
            # time.sleep(2.0)
            # app.mqtt_client.send_message("red", "off")
            # time.sleep(2.0)
            
    except KeyboardInterrupt:
        print("Exiting...")
        app.mqtt_client.close()

main()
