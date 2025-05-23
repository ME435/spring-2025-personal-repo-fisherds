"""
Authors:  Dave Fisher and Dave Fisher.
"""

import time
from rosebot import RoseBot

def main():
    """ Calls the desired TEST functions. """
    run_test_drive_system()


def run_test_drive_system():
    """ Test a robot's DRIVE SYSTEM. """
    print()
    print('--------------------------------------------------')
    print('Testing the  DRIVE SYSTEM  of a robot')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # Construct a robot, that is, a rosebot.RoseBot() object.
    # -------------------------------------------------------------------------
    robot = RoseBot()

    # -------------------------------------------------------------------------
    # STUDENTS: Do the work in this module as follows.
    #   Otherwise, you will be overwhelmed by the number of tests happening.
    #
    #   For each function that you implement:
    #     1. Locate the statements just below this comment that call TEST functions.
    #     2. UN-comment only one test at a time.
    #     3. Implement that function per its _TODO_.
    #     4. Implement as needed the appropriate class methods
    #     5. When satisfied with your work, move onto the next test,
    #        RE-commenting out the previous test to reduce the testing.
    # -------------------------------------------------------------------------

    # run_test_go_stop(robot)
    run_test_go_straight_for_seconds(robot)
    # run_test_go_straight_for_inches(robot)
    # run_test_spin_in_place_for_seconds(robot)
    # run_test_spin_in_place_for_degrees(robot)
    # run_test_draw_polygon(robot)


def run_test_go_stop(robot):
    """
    Tests the   go    and   stop   methods of the DriveSystem class.
    """
    print('--------------------------------------------------')
    print('Testing the  go   and  stop methods of a robot')
    print('--------------------------------------------------')
    # -------------------------------------------------------------------------
    # Get the wheel speeds for this set of tests.
    # -------------------------------------------------------------------------
    while True:
        print("Wheel speeds should be integers between -100 and 100.")
        print("Enter values of 0 for both to exit.")
        left_wheel_speed = int(input("Enter an integer for left wheel speed: "))
        right_wheel_speed = int(input("Enter an integer for right wheel speed: "))
        if left_wheel_speed == 0 and right_wheel_speed == 0:
            break
        print()
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # Call the  go  method of the   drive_system   of the robot,
        #   sending it the two wheel speeds.  Keep going (time.sleep) for 3 seconds.
        #   Then call the  stop  method of the   drive_system   of the robot.
        # -------------------------------------------------------------------------
        robot.drive_system.go(left_wheel_speed, right_wheel_speed)
        time.sleep(3)
        robot.drive_system.stop()
        print("The robot should have stopped moving.")
    
    robot.drive_system.close()  # Problaby not required, but good practice.



def run_test_go_straight_for_seconds(robot):
    """
    Tests the   go_straight_for_seconds   method of the DriveSystem class.
    """
    print('--------------------------------------------------')
    print('Testing the  go_straight_for_seconds method of a robot')
    print('--------------------------------------------------')
    while True:
        print()
        print("Wheel speeds should be integers between -100 and 100.")
        print("Enter a value of 0 to exit.")
        speed = int(input("Enter an integer for wheel speed: "))
        print("Enter a value of 0 to exit.")
        if speed == 0:
            break
        seconds = float(input("Enter how many seconds to go (e.g., 2.3): "))
        if seconds == 0:
            break
        direction = float(input("Direction (e.g., 90): "))
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # Call the  go_straight_for_seconds  method of the   drive_system
        #  of the robot, sending it the input  seconds  and  speed.
        # -------------------------------------------------------------------------
        # robot.drive_system.go_straight_for_seconds(seconds, speed)
        
        # Hacky testing!
        # robot.drive_system.strafe_left(speed)
        # robot.drive_system.strafe_right(speed)
        # time.sleep(seconds)
        # robot.drive_system.stop()
        
        robot.drive_system.move_in_direction(speed, direction)
        time.sleep(seconds)
        robot.drive_system.stop() 
        print("The robot should have stopped moving.")
        
    robot.drive_system.close()  # Problaby not required, but good practice.


def run_test_go_straight_for_inches(robot):
    """
    Tests the   go_straight_for_inches   method of the DriveSystem class.
    """
    print('--------------------------------------------------')
    print('Testing the  go_straight_for_inches method of a robot')
    print('--------------------------------------------------')
    print("Wheel speeds should be integers between -100 and 100.")
    print("Enter a value of 0 to exit.")
    while True:
        print()
        speed = int(input("Enter an integer for wheel speed: "))
        if speed == 0:
            break
        inches = float(input("Enter how many inches to go (e.g., 12.4): "))
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # Call the  go_straight_for_inches  method of the   drive_system
        #  of the robot, sending it the input  inches  and  speed.
        #  (The go_straight_for_inches method uses the same speed for both wheels.)
        # -------------------------------------------------------------------------
        robot.drive_system.go_straight_for_inches(inches, speed)
        print("The robot should have stopped moving.")
        
    robot.drive_system.close()  # Problaby not required, but good practice.

def run_test_spin_in_place_for_seconds(robot):
    """
    Tests the   spin_in_place_for_seconds   method of the DriveSystem class.
    """
    print('--------------------------------------------------')
    print('Testing the  spin_in_place_for_seconds method of a robot')
    print('--------------------------------------------------')
    print("Wheel speeds should be integers between -100 and 100.")
    print("Enter a value of 0 to exit.")
    while True:
        print()
        speed = int(input("Enter an integer for wheel speed: "))
        if speed == 0:
            break
        seconds = float(input("Enter how many seconds to go (e.g., 2.3): "))
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # Call the  spin_in_place_for_seconds  method of the   drive_system
        #  of the robot, sending it the input  seconds  and  speed.
        #  (The go_straight_for_inches method uses the same speed for both wheels.)
        # -------------------------------------------------------------------------
        robot.drive_system.spin_in_place_for_seconds(seconds, speed, isLeftSpin=False)
        print("The robot should have stopped moving.")
        
    robot.drive_system.close()  # Problaby not required, but good practice.


def run_test_spin_in_place_for_degrees(robot):
    """
    Tests the   spin_in_place_for_degrees   method of the DriveSystem class.
    """
    print('--------------------------------------------------')
    print('Testing the  spin_in_place_for_degrees method of a robot')
    print('--------------------------------------------------')
    while True:
        print()
        speed = int(input("Enter an integer for wheel speed: "))
        if speed == 0:
            break
        degrees = float(input("Enter how many degrees to go (e.g., 360): "))
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 7. Call the  spin_in_place_for_degrees  method of the   drive_system
        #  of the robot, sending it the input  degrees  and  speed.
        # -------------------------------------------------------------------------


def run_test_turn_for_seconds(robot):
    """
    Tests the   turn_for_seconds   method of the DriveSystem class.
    """
    print('--------------------------------------------------')
    print('Testing the  turn_for_seconds method of a robot')
    print('--------------------------------------------------')
    while True:
        print()
        speed = int(input("Enter an integer for wheel speed: "))
        if speed == 0:
            break
        seconds = float(input("Enter how many seconds to go (e.g., 2.3): "))
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 8. Call the  turn_for_seconds  method of the   drive_system
        #  of the robot, sending it the input  degrees  and  seconds.
        # -------------------------------------------------------------------------


def run_test_turn_for_degrees(robot):
    """
    Tests the   turn_for_degrees   method of the DriveSystem class.
    """
    print('--------------------------------------------------')
    print('Testing the  turn_for_degrees  method of a robot')
    print('--------------------------------------------------')
    while True:
        print()
        speed = int(input("Enter an integer for wheel speed: "))
        if speed == 0:
            break
        degrees = float(input("Enter how many degrees to go (e.g., 360): "))
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 9. Call the  turn_for_degrees  method of the   drive_system
        #  of the robot, sending it the input  degrees  and  speed.
        # -------------------------------------------------------------------------


def run_test_draw_polygon(robot):
    """
    Uses the methods turn_for_degrees and go_straight_for_inches of the DriveSystem
     to create a small program. This program will ask the user for how many sides they
     would like in their polygon, the length of each side, and a speed.
    Then your robot will drive that polygon shape.
    """
    print('--------------------------------------------------')
    print(' Draw Polygon   ')
    print('--------------------------------------------------')
    while True:
        print()
        speed = int(input("Enter an integer for wheel speed: "))
        if speed == 0:
            break
        sides = int(input("Number of sides (e.g., 6): "))
        # Try a negative value for Number of sides to drive CW around the polygon.
        if sides == 0:
            break
        degrees = 360 / sides
        inches = int(input("Length of each edge in inches (e.g., 8): "))
        if inches == 0:
            break
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 10. Use a loop and call the  spin_in_place_for_degrees and go_straight_for_inches
        #  methods of the   drive_system as needed to draw the polygon,
        #  sending the inputs degrees and speed or inches and speed as appropriate.
        # -------------------------------------------------------------------------



main()
