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
        line_pin_right = 14
        line_pin_middle = 15
        line_pin_left = 23
        self.left_sensor = gz.LineSensor(line_pin_left)
        self.middle_sensor = gz.LineSensor(line_pin_middle)
        self.right_sensor = gz.LineSensor(line_pin_right)
    
    def get_left(self):
        # 0 should be black, but 1 is black
        # 1 should be white, but 0 is white
        if self.left_sensor.value == 1:
            return "B"
        return "W"
    
    def get_middle(self):
        if self.middle_sensor.value == 1:
            return "B"
        return "W"
    
    def get_right(self):
        if self.right_sensor.value == 1:
            return "B"
        return "W"
    
    def is_line(self):
        return (self.get_left() == "B" or 
                self.get_middle() == "B" or 
                self.get_right() == "B")


def main():
    print("Local testing for the two sensor types")
    # test_sensor = UltraSonic()
    # while True:
    #     print(f"Distance in meters = {test_sensor.get()}")
    #     time.sleep(2.0)

    test_sensor = LineSensors()
    while True:
        print(f"Left = {test_sensor.get_left()}  Right = {test_sensor.get_right()}")
        time.sleep(2.0)

if __name__ == "__main__":
    main()
