from spi_ledpixel import Freenove_SPI_LedPixel
import time

class CarLeds:
    
    def __init__(self):
        self.neopixel_strip = Freenove_SPI_LedPixel(count=8, bright=128)
    
    def set_all_leds(self, red, green, blue):
        self.neopixel_strip.set_all_led_color(red, green, blue)
        # self.neopixel_strip.show()
    
    def set_led(self, led_index, red, green, blue):
        self.neopixel_strip.set_led_color(led_index, red, green, blue)
        # self.neopixel_strip.show()

    def turn_off(self):
        self.set_all_leds(0, 0, 0)


if __name__ == "__main__":
    print("Test LED program")
    car_leds = CarLeds()
    car_leds.neopixel_strip.spi_gpio_info()
    car_leds.set_all_leds(255, 0, 0)  # Set all LEDs to red
    time.sleep(1)
    car_leds.set_led(0, 0, 255, 0)    # Set LED 0 to green
    time.sleep(1)
    car_leds.set_led(1, 0, 0, 255)    # Set LED 1 to blue
    time.sleep(1)
    car_leds.set_led(2, 255, 255, 0)  # Set LED 2 to yellow
    time.sleep(4)
    car_leds.turn_off()              # Turn off all LEDs
    print("Done")