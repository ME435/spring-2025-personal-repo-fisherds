import gpiozero as gz
import time
import warnings

class Ultrasonic:

    def __init__(self):
        warnings.filterwarnings("ignore", category = gz.PWMSoftwareFallback)  # Ignore PWM software fallback warnings

        self.distance_sensor = gz.DistanceSensor(echo=22, trigger=27)

    def get_cm(self):
        return self.distance_sensor.distance * 100


class LineSensors:
    
    def __init__(self):
        self.was_line_left = True   # Default value
        self.left = gz.LineSensor(14)
        self.middle = gz.LineSensor(15)
        self.right = gz.LineSensor(23)
    
    def get_left(self):
        if self.left.value == 1:
            return "B"
        return "W"
    
    def get_middle(self):
        if self.middle.value == 1:
            return "B"
        return "W"
    
    def get_right(self):
        if self.right.value == 1:
            return "B"
        return "W"
    
    def get_lineword(self):
        return self.get_left() + self.get_middle() + self.get_right()
    
    def get_value(self):
        lineword = self.get_lineword()
        if lineword == "WWW":
            if self.was_line_left:
                return -3
            return 3
        elif lineword == "BWW":
            self.was_line_left = True
            return -2
        elif lineword == "BBW":
            self.was_line_left = True
            return -1
        elif lineword == "WBW":
            return 0
        elif lineword == "WBB":
            self.was_line_left = False
            return 1
        elif lineword == "WWB":
            self.was_line_left = False
            return 2
        else:
            return 0  # Weird cases BWB or BBB


if __name__ == "__main__":
    print("Local testing for the two sensor types")
    
    ultrasonic = Ultrasonic()
    line_sensors = LineSensors()
    try:
        while True:
            print(f"Distance in cm = {ultrasonic.get_cm()}")
            print(f"Line word = {line_sensors.get_lineword()}  value = {line_sensors.get_value()}")
            time.sleep(2.0)
    except KeyboardInterrupt:
        print("End of program")