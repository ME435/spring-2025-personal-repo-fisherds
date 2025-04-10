import gpiozero as gz
import time
import signal


def main():
    print("Pushbuttons")
    # buttons_using_states()
    buttons_using_events()

def say_hello():
    print("Hello")

def say_goodbye():
    print("Goodbye")

def turn_on_leds(r, y, g):
    r.on()
    y.on()
    g.on()

def turn_off_leds(r, y, g):
    r.off()
    y.off()
    g.off()

def print_names(names, led):
    print("Printing names")
    led.on()
    print("Hello", names)
    # for name in names:
    #     print("Hello", name)
    time.sleep(1.0)
    led.off()

def buttons_using_events():
    print("Button Events")
    button = gz.Button(25)
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    # button.when_pressed = say_hello
    # button.when_released = say_goodbye

    # button.when_pressed = lambda : turn_on_leds(red_led, yellow_led, green_led)
    # button.when_released = lambda : turn_off_leds(red_led, yellow_led, green_led)

    names = []
    button.when_pressed = lambda : names.append("Dave")
    button.when_released = lambda : print_names(names, red_led)

    signal.pause()
    

def buttons_using_states():
    print("Button States")
    # Turn the LED on when the button pressed, otherwise off
    button = gz.Button(25)
    red_led = gz.LED(14)

    while True:
        if button.is_pressed:
            red_led.on()
        else:
            red_led.off()


main()
