import gpiozero as gz
import time
import signal


def main():
    print("Fancy LEDs")
    # fancy_blink()  # Together
    # led_pwm()
    # led_board()
    fancy_traffic_light()


def fancy_blink():
    print("Fancy Blink")
    red_led = gz.LED(14)
    red_led.blink(on_time=1.0, off_time=0.2)  # On for 1 second, off for only .2 seconds
    signal.pause()


def led_pwm():
    print("LED PWM")
    # Goal: Slowly make the LED brighter over 3 seconds, then dim over 3 seconds
    red_pwm_led = gz.PWMLED(14)

    # red_pwm_led.value = 0.5
    # time.sleep(3.0)

    # while True:
    #     for k in range(30):
    #         red_pwm_led.value = k / 30
    #         time.sleep(0.1)
    #     for k in range(30):
    #         red_pwm_led.value = (30 - k) / 30
    #         time.sleep(0.1)

    red_pwm_led.pulse(fade_in_time=3.0, fade_out_time=3.0)
    signal.pause()

def led_board():
    print("LED Board")
    # Goal: Make an LEDBoard with all the LEDs and do stuff!

    # Loop Forever
    #   All on for a second
    #   Only red and green on for a second
    #   Task #2: Make all LEDs on at a 40% brightness for a second
    #   All off for a second

    leds = gz.LEDBoard(14, 15, 18, pwm=True)

    while True:    
        leds.on()
        time.sleep(1.0)
        leds.value = (1, 0, 1)
        time.sleep(1.0)
        leds.value = (0.4, 0.4, 0.4)
        time.sleep(1.0)
        leds.off()
        time.sleep(1.0)


def fancy_traffic_light():
    print("Fancy Traffic Light") 
    # Goal: Same goal as the manual traffic light but using TrafficLights

    # red_led = gz.LED(14)
    # yellow_led = gz.LED(15)
    # green_led = gz.LED(18)
    traffic_light = gz.TrafficLights(14, 15, 18)

    # Loop forever
    #   Green LED on only for 4 seconds
    #   Yellow LED on only for 1 second
    #   Red LED on only for 3 seconds

    while True:
        traffic_light.green.on()
        time.sleep(4.0)
        traffic_light.green.off()

        traffic_light.amber.on()
        time.sleep(1.0)
        traffic_light.amber.off()

        traffic_light.red.on()
        time.sleep(3.0)
        traffic_light.red.off()
        

main()
