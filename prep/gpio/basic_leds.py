import gpiozero as gz
import time


def main():
    print("LED Basics")
    # output_on_off()
    traffic_light()


def traffic_light():
    print("Traffic Light")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    # Loop forever
    #   Green LED on only for 4 seconds
    #   Yellow LED on only for 1 second
    #   Red LED on only for 3 seconds

    while True:
        green_led.on()
        time.sleep(4.0)
        green_led.off()

        yellow_led.on()
        time.sleep(1.0)
        yellow_led.off()

        red_led.on()
        time.sleep(3.0)
        red_led.off()
        

def output_on_off():
    print("Output On Off")
    # red_led = gz.DigitalOutputDevice(14)  # for motors, LEDs, lamp, 
    red_led = gz.LED(14)  # subclass

    for k in range(5):
        # Goal on for a second, off for a second, 5 times
        red_led.on()
        # red_led.value = 1  # an alternative
        time.sleep(1.0)
        red_led.off()
        time.sleep(1.0)

main()
