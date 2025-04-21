
from led import Led
import time

print("Lights")
my_led = Led()
my_led.ledIndex(0, 255, 0, 0)
my_led.ledIndex(3, 255, 0, 0)
my_led.ledIndex(7, 255, 0, 0)
               
time.sleep(3)
print("Goodbye")