import time
from rpi_ws281x import PixelStrip, Color

# sudo .venv/bin/python my_led_test.py 

# LED strip configuration:
LED_COUNT = 8         # Number of LEDs in the strip
LED_PIN = 18           # GPIO pin connected to the LED strip (must support PWM)
LED_FREQ_HZ = 800000  # Frequency of the PWM signal (typically 800kHz for WS2812)
LED_DMA = 10           # DMA channel to use for PWM (usually 10)
LED_BRIGHTNESS = 255   # Brightness of the LEDs (0-255)
LED_INVERT = False     # True to invert the signal (if necessary)

# Initialize the LED strip
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

# Set the color of each LED to red
def color_wipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

# Create a red color
red = Color(255, 0, 0)

# Run the color wipe function to display red on all LEDs
color_wipe(strip, red)
