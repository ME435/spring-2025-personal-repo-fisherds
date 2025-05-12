from spi_ledpixel import Freenove_SPI_LedPixel
import gpiozero as gz
import time

class CarLeds:
    
    def __init__(self):
        # Test that had no effect!
        # pin18 = gz.InputDevice(18, pull_up=False)  # GPIO pin 18 out of the way
        self.neopixel_strip = Freenove_SPI_LedPixel(bright=128)

    def set_all_leds(self, red, green, blue):
        self.neopixel_strip.set_all_led_color(red, green, blue)        

    def set_led(self, led_index, red, green, blue):
        self.neopixel_strip.set_led_color(led_index, red, green, blue)        

    def turn_off(self):
        self.set_all_leds(0, 0, 0)


if __name__ == "__main__":
    car_leds = CarLeds()
    car_leds.set_all_leds(255, 0, 0)  # Set all LEDs to red
    time.sleep(1)                     # Wait for 1 second
    car_leds.set_led(0, 0, 255, 0)     # Set LED at index 0 to green
    time.sleep(1)                     # Wait for 1 second
    car_leds.set_led(1, 0, 0, 255)     # Set LED at index 1 to blue
    time.sleep(4)                     # Wait for 1 second
    car_leds.turn_off()                # Turn off all LEDs