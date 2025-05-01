from servo import Servo
import time


class ServoHead:
    
    def __init__(self):
        self.servos = Servo()
        self.reset()
    
    def set_pan_position(self, degrees):
        self.servos.set_servo_pwm('0', degrees)
    
    def set_tilt_position(self, degrees):
        self.servos.set_servo_pwm('1', degrees)
    
    def reset(self):
        self.servos.set_servo_pwm('0', 90)
        self.servos.set_servo_pwm('1', 90)

if __name__ == "__main__":
    servo_head = ServoHead()
    
    try:
        print ("Program is starting ...")
        while True:
            for i in range(50,110,1):
                servo_head.set_pan_position(i)
                time.sleep(0.01)
            for i in range(110,50,-1):
                servo_head.set_pan_position(i)
                time.sleep(0.01)
            for i in range(80,150,1):
                servo_head.set_tilt_position(i)
                time.sleep(0.01)
            for i in range(150,80,-1):
                servo_head.set_tilt_position(i)
                time.sleep(0.01)   
    except KeyboardInterrupt:
        print ("\nEnd of program")
        servo_head.reset()
    