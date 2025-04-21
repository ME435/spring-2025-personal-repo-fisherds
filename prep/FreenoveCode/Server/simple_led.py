import time
from rpi_ws281x import PixelStrip, Color

# sudo .venv/bin/python simple_led.py 

# LED strip configuration:
LED_COUNT = 8       # Number of LED pixels.
LED_PIN = 18        # GPIO pin (must support PWM!).
LED_BRIGHTNESS = 50
LED_CHANNEL = 0

strip = PixelStrip(LED_COUNT, LED_PIN, brightness=LED_BRIGHTNESS, channel=LED_CHANNEL)
strip.begin()

# Set first LED to red
print("Setting LED 0 to red")
strip.setPixelColor(0, Color(255, 0, 0))
strip.show()
time.sleep(2)

# Turn off
print("Setting LED 0 off")
strip.setPixelColor(0, Color(0, 0, 0))
strip.show()
