import gpiozero as gz
import time
import signal

fuction_using_lambda = lambda: print("Function using lambda")

def fuction_using_def():
    print("Function using def")
    print("As many lines of code as you want")

def some_helper_function(led_board, brightness):
    print("Some helper function")
    led_board.value = (brightness, 0, brightness)
    time.sleep(1)
    led_board.value = (0, 0, 0)
    time.sleep(1)

def button_events():
    print("Button Events")
    button = gz.Button(25)
    led_board = gz.LEDBoard(14, 15, 18, pwm=True)
    # button.when_pressed = lambda: print("Button pressed")
    # button.when_released = lambda: print("Button released")
    # button.when_held = lambda: print("Button held")
    
    button.when_pressed = fuction_using_def
    button.when_released = fuction_using_lambda
    button.when_held = lambda: some_helper_function(led_board, 0.5)
    signal.pause()

def button_states():
    print("Button States")
    button = gz.Button(25)
    
    while True:
        if button.is_pressed:
            print("Button is pressed")
        else:
            print("Button is not pressed")
        time.sleep(0.5)

def main():
    print("Pushbuttons")
    # button_states()
    button_events()
    
main()
