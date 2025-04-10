import gpiozero as gz
import time
import signal

def led_board():
    print("LED Board")
    
    # Construct an LED Board object
    led_board = gz.LEDBoard(red=14, yellow=15, green=18, pwm=True)
    
    # Loop 4 times
    for _ in range(4):
        # All on for 1 second
        led_board.on()
        time.sleep(1)
        
        # Red and Green on for 1 second
        led_board.red.on()
        led_board.green.on()
        led_board.yellow.off()
        time.sleep(1)
        
        # Green on at 0.5 brightness for 1 second
        led_board.off()
        led_board.green.value = 0.5
        time.sleep(1)
        
        # All off
        led_board.off()
        time.sleep(1)
    

def led_pwm():
    print("LED PWM")
    red_led = gz.PWMLED(14)
    yellow_led = gz.PWMLED(15)
    green_led = gz.PWMLED(18)
    
    # red_led.value = 0.25
    # time.sleep(1)
    # red_led.value = 0.5
    # time.sleep(1)
    # red_led.value = 0.75
    # time.sleep(1)
    # red_led.value = 1.0
    # time.sleep(1)
    
    # red_led.pulse(fade_in_time=3.0, fade_out_time=0.5, n=3, background=False)
    red_led.pulse(fade_in_time=3.0, fade_out_time=0.5)
    yellow_led.pulse(fade_in_time=4.0, fade_out_time=0.5)
    green_led.pulse(fade_in_time=5.0, fade_out_time=0.5)
    signal.pause()


def fancy_blink():
    print("Fancy blink")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)
    
    red_led.blink(on_time=0.5, off_time=0.5)
    time.sleep(0.15)
    yellow_led.blink(on_time=0.5, off_time=0.5)
    time.sleep(0.3)
    green_led.blink(on_time=0.5, off_time=0.5)
    # time.sleep(5)
    signal.pause()

def traffic_light():
    print("Manual traffic light")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    # Loop forever
    #   Green LED on only for 4 seconds
    #   Yellow LED on only for 1 second
    #   Red LED on only for 3 seconds

    
def basic_on_off():
    print("Basic On/Off")
    red_led = gz.DigitalOutputDevice(14)
    yellow_led = gz.DigitalOutputDevice(15)
    green_led = gz.DigitalOutputDevice(18)
    
    for k in range(3):
        red_led.on()
        yellow_led.on()
        green_led.on()
        print("On")
        time.sleep(3)
        print("Off")
        red_led.off()
        yellow_led.off()
        green_led.off()
        
        time.sleep(1)

def main():
    print("LEDs")
    # basic_on_off()
    # traffic_light()
    # fancy_blink()
    # led_pwm()
    led_board()
    
    print("Goodbye!")
    
main()
