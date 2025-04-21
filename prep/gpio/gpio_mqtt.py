import mqtt_helper as mh
import time
import gpiozero as gz

class App:

    def __init__(self):
        print("Using MQTT with a class")

        self.red_led = gz.LED(14)   # 17
        self.yellow_led = gz.LED(15)   # 18
        self.green_led = gz.LED(18)  #27


        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="fisherds/to_pi",
                            publish_topic_name="fisherds/to_comp",
                            use_off_campus_broker=True)
        self.mqtt_client.callback = self.mqtt_callback

        self.button25 = gz.Button(25)
        self.button25.when_pressed = lambda : self.mqtt_client.send_message("button") 
        self.button23 = gz.Button(23)
        self.button23.when_pressed = lambda : self.mqtt_client.send_message("reset") 

    def mqtt_callback(self, message_type, payload):
        print("Received type:", message_type)
        print("Received payload:", payload)

        if message_type == "red":
            if payload == "on":
                self.red_led.on()
            if payload == "off":
                self.red_led.off()

        if message_type == "yellow":
            if payload == 1:
                self.yellow_led.on()
            if payload == 0:
                self.yellow_led.off()
                
        if message_type == "green":
            if payload:
                self.green_led.on()
            if not payload:
                self.green_led.off()


        if message_type == "leds":
            if payload[0] == 1:
                self.red_led.on()
            if payload[0] == 0:
                self.red_led.off()
            if payload[1] == 1:
                self.yellow_led.on()
            if payload[1] == 0:
                self.yellow_led.off()
            if payload[2] == 1:
                self.green_led.on()
            if payload[2] == 0:
                self.green_led.off()
                
def main():
    print("GPIO MQTT")
    app = App()

    while True:
        time.sleep(0.1)
        # print("Sending on")
        # app.mqtt_client.send_message("red", "on")
        # app.mqtt_client.send_message("yellow", 1)
        # app.mqtt_client.send_message("green", True)
        # time.sleep(2.0)
        # print("sending off")
        # app.mqtt_client.send_message("red", "off")
        # app.mqtt_client.send_message("yellow", 0)
        # app.mqtt_client.send_message("green", False)
        # time.sleep(2.0)

        # app.mqtt_client.send_message("leds", [1, 0, 1])
        # time.sleep(2.0)
        # app.mqtt_client.send_message("leds", [0, 1, 0])
        # time.sleep(2.0)


main()