from servo import Servo
import time


class ServoHead:
    
    def __init__(self):
        self.servos = Servo()
    
    def set_pan_angle(self, degrees):
        self.servos.set_servo_pwm('0', degrees)
    
    def set_tilt_angle(self, degrees):
        self.servos.set_servo_pwm('1', degrees)
    
    def reset(self):
        self.set_pan_angle(90)
        self.set_tilt_angle(90)

if __name__ == "__main__":
    print("Servo head test program.")
    servo_head = ServoHead()
    try:
        while True:
            servo_head.reset()
            time.sleep(1)
            
            # Pan test
            servo_head.set_pan_angle(30)
            time.sleep(1)
            servo_head.set_pan_angle(150)
            time.sleep(2)
            servo_head.set_pan_angle(90)
            
            # Titl test
            servo_head.set_tilt_angle(70)
            time.sleep(1)
            servo_head.set_tilt_angle(160)
            time.sleep(1)
            servo_head.set_tilt_angle(90)
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nEnd of program")
        servo_head.reset()