from motor import OrdinaryCar
import time
import math

class DriveSystem:
    
    def __init__(self):
        self.car = OrdinaryCar()
    
    def scale_speed(self, speed):
        return int(speed / 100 * 4095 )
    
    def set_speeds(self, lf, lr, rf, rr):
        self.car.set_motor_model(self.scale_speed(lf), self.scale_speed(lr),
                                 self.scale_speed(rf), self.scale_speed(rr))
    
    def go(self, left_speed, right_speed):
        self.set_speeds(left_speed, left_speed, right_speed, right_speed)
    
    def stop(self):
        self.set_speeds(0, 0, 0, 0)
    
    def strafe_left(self, speed):
        duty = self.scale_speed(speed)
        self.car.set_motor_model(-duty, duty, duty, -duty)
    
    def strafe_right(self, speed):
        self.strafe_left(-speed)
    
    def go_straight_for_seconds(self, seconds, speed):
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()
        
    def go_straight_for_inches(self, inches, speed):
        # TODO as part of Lab 4A: Run a few experiments to determine speed in inches per second
        m = 1
        B = 0
        inches_per_second = m * speed + B
        seconds = inches / inches_per_second
        self.go_straight_for_seconds(seconds, speed)
    
    def spin_in_place_for_seconds(self, seconds, speed, isLeftSpin=True):
        duty = self.scale_speed(speed)
        if isLeftSpin:
            self.car.set_motor_model(-duty, -duty, duty, duty)
        else:
            self.car.set_motor_model(duty, duty, -duty, -duty)
        time.sleep(seconds)
        self.stop()
        
    def spin_in_place_for_degrees(self, degrees, speed, isLeftSpin=True):
        # TODO as part of Lab 4A: Run a few experiments to determine speed in degrees per second
        m = 1
        B = 0
        degrees_per_second = m * speed + B
        seconds = inches / degrees_per_second
        self.spin_in_place_for_seconds(seconds, speed, isLeftSpin)


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
        self.car.set_motor_model(self.scale_speed(fl), self.scale_speed(rl), self.scale_speed(fr), self.scale_speed(rr))

    def strafe_circle(self, speed, duration_seconds):
        steps = 100  # More steps = smoother circle
        angle_step = 360 / steps
        delay = duration_seconds / steps

        for i in range(steps):
            angle = i * angle_step
            self.move_in_direction(speed, angle)
            time.sleep(delay)

        self.stop()
                
    def stop(self):
        self.car.set_motor_model(0, 0, 0, 0)
        
    def close(self):
        self.car.close()


if __name__ == '__main__':
    drive_system = DriveSystem()
    try:
        # drive_system.go_straight_for_seconds(2, 50)
        # drive_system.strafe_left(50)
        # time.sleep(1)
        # drive_system.strafe_right(50)
        # time.sleep(1)
        # drive_system.spin_in_place_for_seconds(2, 50, True)
        # drive_system.spin_in_place_for_seconds(2, 50, False)
        # drive_system.move_in_direction(50, 45)
        # time.sleep(2)
        drive_system.strafe_circle(50, 5)
    finally:
        drive_system.close()