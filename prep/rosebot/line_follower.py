from rosebot import RoseBot
import time


def main():
    robot = RoseBot()
    parameters = [
        [-30, 30, 0], # Line = -3: left front, right front, both back
        [-20, 30, 10], # Line = -2: left front, right front, both back
        [-10, 30, 20],  # Line = -1: left front, right front, both back
        [30, 30, 30],  # Line =  0: left front, right front, both back
        [30, -10, 20], # Line =  1: left front, right front, both back
        [30, -20, 10], # Line =  2: left front, right front, both back
        [30, -30, 0],  # Line =  3: left front, right front, both back
    ]
    scaling = 1.0
    debug = True
    while True:
        if robot.ultrasonic.get_distance_in_meters() < 0.5:
            if debug:
                print("Obstacle detected, stopping the robot.")
            robot.drive_system.stop()
        else:
            line_value = robot.line_sensors.get_line_value()
            parameter_index = 3 + line_value  # -3 to 3 is now 0 to 6
            lf = int(parameters[parameter_index][0] * scaling)
            lr = int(parameters[parameter_index][2] * scaling)
            rf = int(parameters[parameter_index][1] * scaling)
            rr = int(parameters[parameter_index][2] * scaling)
            if debug:
                print(f"Line Follow {line_value} values to drive", lf, lr, rf, rr)
            robot.drive_system.set_speeds(lf, lr, rf, rr)
        if debug:
            time.sleep(2.0)
        else:
            time.sleep(0.05)
            
            
main()
