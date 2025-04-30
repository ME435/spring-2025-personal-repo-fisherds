from spi_ledpixel import Freenove_SPI_LedPixel
import time

class CarLeds:
    def __init__(self):
        self.leds = Freenove_SPI_LedPixel(count=8, bright=128)  # 128 = half brightness

    def turn_off(self):
        self.set_all_leds(0, 0, 0)

    def set_all_leds(self, red, green, blue):
        self.leds.set_all_led_color_data(red, green, blue)
        self.leds.show()
    
    def set_led(self, led_index, red, green, blue):
        self.leds.set_ledpixel(led_index, red, green, blue)
        self.leds.show()


if __name__ == "__main__":
    print("Car Leds")
    car_leds = CarLeds()
    
    car_leds.set_all_leds(255, 0, 0)
    time.sleep(0.5)
    car_leds.set_all_leds(0, 255, 0)
    time.sleep(0.5)    
    car_leds.set_all_leds(0, 0, 255)
    time.sleep(0.5)
    car_leds.set_all_leds(0, 255, 255)
    time.sleep(0.5)
    car_leds.set_all_leds(0, 0, 0)
    time.sleep(0.5)
    
    try:        
        for i in range(8):
            car_leds.set_led(i, 255, 0, 0)  # Set LED to red
            time.sleep(0.5)
            car_leds.set_led(i, 0, 255, 0)  # Set LED to green
            time.sleep(0.5)
            car_leds.set_led(i, 0, 0, 255)  # Set LED to blue
            time.sleep(0.5)
        car_leds.turn_off()
    except KeyboardInterrupt:
        print("Exiting...")
        for i in range(8):
            car_leds.set_led(i, 0, 0, 0)
        car_leds.leds.show()
