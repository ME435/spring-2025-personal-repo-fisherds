from motor import OrdinaryCar
import time


class DriveSystem:

    def __init__(self):
        self.car = OrdinaryCar()
    
    def go(self, left_speed, right_speed):
        left_duty = int(left_speed / 100 * 4095)
        right_duty = int(right_speed / 100 * 4095)
        self.car.set_motor_model(left_duty, left_duty, right_duty, right_duty)

    def stop(self):
        self.car.set_motor_model(0, 0, 0, 0)

    def strafe_left(self, speed):
        duty = int(speed / 100 * 4095)
        self.car.set_motor_model(-duty, duty, duty, -duty)

    def strafe_right(self, speed):
        duty = int(speed / 100 * 4095)
        self.car.set_motor_model(duty, -duty, -duty, duty)
        
    def go_straight_for_seconds(self, speed, seconds):
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()
    
    def go_straight_for_inches(self, speed, inches):
        # Convert a number inches into seconds
        inches_per_second = 0.172 * speed + 2.15
        # TODO: Use this to get seconds...
        self.go_straight_for_seconds(speed, inches / inches_per_second)
    
    def close(self):
        self.car.close()
        print("Drive system closed")



if __name__ == "__main__":
    ds = DriveSystem()
    try:
        ds.strafe_right(50)
        time.sleep(0.8)
        ds.stop()
        print("Stopping")

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print ("\nEnd of program")
    finally:
        ds.close()
