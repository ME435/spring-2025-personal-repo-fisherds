import gpiozero as gz
from mqtt_helper import MqttClient
import time

class App:
    def __init__(self):
        self.led_board = gz.LEDBoard(red=14, yellow=15, green=18, pwm=True)
        
        self.button_23 = gz.Button(23)
        self.button_23.when_pressed = self.button_23_pressed
        self.button_25 = gz.Button(25)
        self.button_25.when_pressed = lambda: self.mqtt_client.send_message("reset")
        
        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/fisherds/#",  # Could also use "me435/fisherds/to_pi"
                                 publish_topic_name="me435/fisherds/to_computer",
                                 use_off_campus_broker=True)
        
    def button_23_pressed(self):
        # print("Button 23 pressed")
        self.mqtt_client.send_message("button")
        
    def mqtt_callback(self, type_name, payload):
        print(f"My Callback: {type_name} - {payload}")
        if type_name == "red":
            if payload == "on":
                self.led_board.red.on()
            elif payload == "off":
                self.led_board.red.off()
                
        if type_name == "yellow":
            if payload == 1:
                self.led_board.yellow.on()
            elif payload == 0:
                self.led_board.yellow.off()
                
        if type_name == "green":
            if payload:
                self.led_board.green.on()
            elif not payload:
                self.led_board.green.off()
                
        if type_name == "leds":
            if payload[0] == 1:
                self.led_board.red.on()
            elif payload[0] == 0:
                self.led_board.red.off()
                
            if payload[1] == 1:
                self.led_board.yellow.on()
            elif payload[1] == 0:
                self.led_board.yellow.off()
                
            if payload[2] == 1:
                self.led_board.green.on()
            elif payload[2] == 0:
                self.led_board.green.off()

def main():
    print("GPIO MQTT Test")
    app = App()
    
    try:
        while True:
            time.sleep(0.1)
            
            # app.mqtt_client.send_message("red", "on")    
            # app.mqtt_client.send_message("yellow", 1)    
            # app.mqtt_client.send_message("green", True)  
            
            # app.mqtt_client.send_message("leds", [1, 0, 1])  
            # time.sleep(2)
            
            # app.mqtt_client.send_message("red", "off")    
            # app.mqtt_client.send_message("yellow", 0)    
            # app.mqtt_client.send_message("green", False) 

            # app.mqtt_client.send_message("leds", [0, 1, 0])   
            # time.sleep(2)


    except KeyboardInterrupt:
        print("Exiting...")
        app.mqtt_client.close()  
          
main()

