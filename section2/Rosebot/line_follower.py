from rosebot import RoseBot
import time

def main():
    print("Line Follower")
    robot = RoseBot()
    
    try:
        while True:
            # Get the ultrasonic sensor reading
            # If the distance is less than 20 cm
            #   stop the robot
            # If the distance is greater than 20 cm, follow the line
            #   Get the line sensor readings
            #   Update the robot's speed based on the line sensor readings
            time.sleep(0.1)
    except KeyboardInterrupt:  # Handle keyboard interrupt (Ctrl+C)
        robot.drive_system.stop()
        robot.drive_system.close()
        print("\nEnd of program")  # Print an end message
        
main()
