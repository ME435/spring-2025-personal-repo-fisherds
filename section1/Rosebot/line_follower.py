from rosebot import RoseBot
import time

def main():
    print("Line Follower")
    robot = RoseBot()
    debug_mode = True
    
    try:

        while True:
            # Check the UltraSonic sensor
            # If less than 20 cm, stop
            # Otherwise, check the line sensors
            # Update the motor speeds based on the line sensors
            
            time.sleep(0.1)
            if debug_mode:
                time.sleep(2)

    except KeyboardInterrupt:  # Handle keyboard interrupt (Ctrl+C)
        robot.drive_system.stop()
        robot.drive_system.close()
        print("\nEnd of program")  # Print an end message


main()
