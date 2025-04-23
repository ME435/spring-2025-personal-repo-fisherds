import gpiozero as gz
import time


class UltraSonic:

    def __init__(self):
        print("Make the Ultrasonic sensor")
        self.distance_sensor = gz.DistanceSensor(echo=22, trigger=27)

    def get(self):
        return self.distance_sensor.distance


class LineSensors:

    def __init__(self):
        print("Make the line sensors (all 3) as a class")
        self.was_left_side = True  # True if line was last seen on left side.
        self.left_sensor = gz.LineSensor(14)
        self.middle_sensor = gz.LineSensor(15)
        self.right_sensor = gz.LineSensor(23)
    
    def get_left(self):
        # 0 should be black???
        # 1 should be white???
        if self.left_sensor.value == 0:
            return "B"
        return "W"
    
    def get_middle(self):
        if self.middle_sensor.value == 0:
            return "B"
        return "W"
    
    def get_right(self):
        if self.right_sensor.value == 0:
            return "B"
        return "W"
    
    def get_line_word(self):
        return self.get_left() + self.get_middle() + self.get_right()
    
    def get_line_value(self):
        lineword = self.get_line_word()
        if lineword == "WWW" and self.was_left_side:
            return -3
        elif lineword == "BWW":
            self.was_left_side = True
            return -2
        elif lineword == "BBW":
            self.was_left_side = True
            return -1
        elif lineword == "WBW":
            return 0
        elif lineword == "WBB":
            self.was_left_side = False
            return 1
        elif lineword == "WWB":
            self.was_left_side = False
            return 2
        elif lineword == "WWW" and not self.was_left_side:
            return 3
        else:
            return 0  # Unexpected case BWB or BBB just go straight for now.
    
    def is_line(self):
        return (self.get_left() == "B" or 
                self.get_middle() == "B" or 
                self.get_right() == "B")


def main():
    print("Local testing for the two sensor types")
    if False:
        test_sensor = UltraSonic()
        while True:
            print(f"Distance in meters = {test_sensor.get()}")
            time.sleep(2.0)

    if True:
        test_sensor = LineSensors()
        while True:
            print(f"Left = {test_sensor.get_left()}  Right = {test_sensor.get_right()}")
            print(f"Line word = {test_sensor.get_line_word()}  value = {test_sensor.get_line_value()}")
            time.sleep(2.0)

if __name__ == "__main__":
    main()
