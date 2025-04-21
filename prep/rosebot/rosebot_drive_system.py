from motor import OrdinaryCar
import time
import math

class DriveSystem:

    def __init__(self):
        self.car = OrdinaryCar()
    
    def _scale_speed(self, value):
        return int((value / 100) * 4095)
    
    def go(self, left_speed, right_speed):
        left_duty = self._scale_speed(left_speed)
        right_duty = self._scale_speed(right_speed)
        self.car.set_motor_model(left_duty, left_duty, right_duty, right_duty)

    def stop(self):
        self.car.set_motor_model(0, 0, 0, 0)
        
    def rotate_left(self, speed):
        duty = self._scale_speed(speed)
        self.car.set_motor_model(-duty, -duty, duty, duty)

    def rotate_right(self, speed):
        duty = self._scale_speed(speed)
        self.car.set_motor_model(duty, duty, -duty, -duty)

    def strafe_left(self, speed):
        duty = self._scale_speed(speed)
        self.car.set_motor_model(-duty, duty, duty, -duty)

    def strafe_right(self, speed):
        duty = self._scale_speed(speed)
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
    
    def move_in_direction(self, speed, angle_in_degrees):
        # Front           Front
        #  Left           Right
        #    \             /
        #     \           /
        #      \         /
        #      [ROBOT BASE]
        #      /         \
        #     /           \
        #    /             \
        # Rear           Rear
        # Left           Right

        angle_rad = math.radians(angle_in_degrees)

        fl = math.sin(angle_rad + math.pi / 4)
        fr = -math.sin(angle_rad - math.pi / 4)
        rl = -math.sin(angle_rad - math.pi / 4)
        rr = math.sin(angle_rad + math.pi / 4)

        # Normalize to keep the maximum magnitude at 1.0
        max_val = max(abs(fl), abs(fr), abs(rl), abs(rr))
        fl = fl / max_val * speed
        fr = fr / max_val * speed
        rl = rl / max_val * speed
        rr = rr / max_val * speed

        # Set motor values
        self.car.set_motor_model(self._scale_speed(fl), self._scale_speed(rl), self._scale_speed(fr), self._scale_speed(rr))

    def strafe_circle(self, speed, duration_seconds):
        steps = 100  # More steps = smoother circle
        angle_step = 360 / steps
        delay = duration_seconds / steps

        for i in range(steps):
            angle = i * angle_step
            self.move_in_direction(angle, speed)
            time.sleep(delay)

        self.stop()

    def close(self):
        self.car.close()
        print("Drive system closed")



if __name__ == "__main__":
    ds = DriveSystem()
    try:
        # ds.strafe_right(50)
        ds.move_in_direction(0, 50)      # Forward
        ds.move_in_direction(90, 50)     # Right
        ds.move_in_direction(180, 50)    # Backward
        ds.move_in_direction(270, 50)    # Left
        ds.move_in_direction(45, 70)     # Diagonal front-right

        time.sleep(0.8)
        ds.stop()
        print("Stopping")

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print ("\nEnd of program")
    finally:
        ds.close()
