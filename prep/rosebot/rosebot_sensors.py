import gpiozero as gz
import time
import warnings
from adc import ADC

class RosebotADC():
    def __init__(self):
        self.adc = ADC()  # Initialize the ADC class

    def get_left_photoresistor(self):
        return self.adc.read_adc(0)  # Read the left photoresistor value

    def get_right_photoresistor(self):
        return self.adc.read_adc(1)  # Read the right photoresistor value

    def get_battery_voltage(self):
        return self.adc.read_adc(2) * (3 if self.adc.pcb_version == 1 else 2)  # Calculate the power value based on the PCB version
    

class UltraSonic:

    def __init__(self):
        warnings.filterwarnings("ignore", category = gz.PWMSoftwareFallback)  # Ignore PWM software fallback warnings
        self.distance_sensor = gz.DistanceSensor(echo=22, trigger=27)

    def get_cm(self):
        distance = self.distance_sensor.distance * 100  # Get the distance in centimeters
        return round(float(distance), 1)  # Return the distance rounded to one decimal place


class LineSensors:

    def __init__(self):
        self.was_left_side = True  # True if line was last seen on left side.
        self.left_sensor = gz.LineSensor(14)
        self.middle_sensor = gz.LineSensor(15)
        self.right_sensor = gz.LineSensor(23)
    
    def get_left(self):
        # 0 is white on this car.
        # 1 is black on this car.
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
    print("Local testing for the sensors")
    
    if True:
        test_sensor = RosebotADC()
        while True:
            print(f"Left = {test_sensor.get_left_photoresistor()}  Right = {test_sensor.get_right_photoresistor()}  Battery = {test_sensor.get_battery_voltage()}")
            time.sleep(2.0)
            
    if False:
        test_sensor = UltraSonic()
        while True:
            print(f"Distance in cm = {test_sensor.get_cm()}")
            time.sleep(2.0)

    if False:
        test_sensor = LineSensors()
        while True:
            print(f"Left = {test_sensor.get_left()}  Right = {test_sensor.get_right()}")
            print(f"Line word = {test_sensor.get_line_word()}  value = {test_sensor.get_line_value()}")
            time.sleep(2.0)

if __name__ == "__main__":
    main()
