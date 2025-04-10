import gpiozero as gz
import time
import signal

def led_board():
    print("LED Board")
    
    # TODO: Construct an LEDBoard
    # Loop 5 times:
    #   Turn on all the LEDs
    #   Wait 1 second
    #   Turn off all the LEDs
    #   Wait 1 second
    #   Turn on just Red and Green
    #   Wait 1 second
    #   Turn on Green at a 0.5 brightness
    #   Wait 1 second
    led_board = gz.LEDBoard(14, 15, 18, pwm=True)
    for k in range(5):
        led_board.on()
        time.sleep(1)
        led_board.off()
        time.sleep(1)
        led_board.value = (1, 0, 1)
        time.sleep(1)
        led_board.value = (0, 0, 0.5)
        time.sleep(1)
    
    

def fancy_leds():
    print("Fancy LEDs")
    red_led = gz.LED(14)    
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)
    
    # red_led.blink(on_time=1.0, off_time=0.5, n=3, background=False)
    red_led.blink(on_time=1.0, off_time=0.5)
    time.sleep(0.15)
    yellow_led.blink(on_time=1.0, off_time=0.5)
    time.sleep(0.3)
    green_led.blink(on_time=1.0, off_time=0.5)
    signal.pause()


def basic_on_off():
    print("Basic on/off")
    red_led = gz.DigitalOutputDevice(14)    
    yellow_led = gz.DigitalOutputDevice(15)
    green_led = gz.DigitalOutputDevice(18)
    
    # red_led.on()
    # yellow_led.on()
    # green_led.on()
    # time.sleep(4)
    
    # TODO: Flash all the LEDs 3 times, on for 3 seconds, off for 1 second
    for i in range(3):
        red_led.on()
        yellow_led.on()
        green_led.on()
        time.sleep(3)
        red_led.off()
        yellow_led.off()
        green_led.off()
        time.sleep(1)

def main():
    print("LEDs")
    # basic_on_off()
    # fancy_leds()
    led_board()
    print("Goodbye")

    
main()
