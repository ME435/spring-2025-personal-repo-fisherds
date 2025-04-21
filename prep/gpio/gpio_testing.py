import gpiozero as gz
import time

# From: https://forums.raspberrypi.com/viewtopic.php?t=360832
# within pyvenv.cfg change this...
# include-system-site-packages = true

# Well, I think I have found an answer.
# In the virtual environment folder that is a file called pyvenv.cfg, In that file there is a line - "include-system-site-packages = false" .
# Changing that line to "include-system-site-packages = true" and the venv now has all the same stuff as the base python.


def main():
    print("gpiozero testing in venv")
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
        


main()
