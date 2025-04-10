import gpiozero as gz
import time
import signal

def helper_function(led_board, state):
    print("Helper function")
    if state == "on":
        led_board.on()
        time.sleep(1)
        led_board.off()
    elif state == "off":
        led_board.off()
    else:
        print("Invalid state")

def passing_stuff_to_lambda():
    print("Passing stuff to lambda")
    button = gz.Button(25)  # GPIO pin 25
    led_board = gz.LEDBoard(red=14, yellow=15, green=18, pwm=True)
    button.when_pressed = lambda: helper_function(led_board, "on")
    button.when_released = lambda: helper_function(led_board, "off")
    signal.pause()


def function_using_def():
    print("def makes a function")
    print("def can have many lines of code")

function_using_lambda = lambda: print("lambda makes a function too, but 1 line only")

def buttons_with_events():
    print("Using callback functions")
    button = gz.Button(25)  # GPIO pin 25
    # button.when_pressed = lambda: print("Button pressed")
    button.when_pressed = function_using_def
    # button.when_released = lambda: print("Button released")
    button.when_released = function_using_lambda
    button.when_held = lambda: print("Button held")
    signal.pause()
    

def read_button_state():
    print("Press the button to see its state.")
    button = gz.Button(25)  # GPIO pin 25
    while True:
        if button.is_pressed:
            print("Button is pressed")
        else:
            print("Button is not pressed")
        time.sleep(0.5)


def main():
    print("Pushbutton example")
    # read_button_state()
    # buttons_with_events()
    passing_stuff_to_lambda()
    
main()