import gpiozero as gz
import warnings
import time
from adc import ADC


class RosebotAdc:
    
    def __init__(self):
        self.adc = ADC()
        
    def get_left_photoresistor(self):
        return self.adc.read_adc(0)
        
    def get_right_photoresistor(self):
        return self.adc.read_adc(1)

    def get_battery_voltage(self):
        return self.adc.read_adc(2) * 2
        # The battery voltage is multiplied by 2 to account for the PCB version.
    
    def close(self):
        self.adc.close_i2c()


class UltraSonic:
    
    def __init__(self):
        warnings.filterwarnings("ignore", category = gz.PWMSoftwareFallback)  # Ignore PWM software fallback warnings
        self.ultrasonic = gz.DistanceSensor(echo=22, trigger=27)
        
    def get_cm(self):        
        return self.ultrasonic.distance * 100  # Convert to cm


class LineSensors:
    
    def __init__(self):
        self.was_last_left = True   # Default for now.
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
            if self.was_last_left:
                return -3
            return 3
        elif lineword == "BWW":
            self.was_last_left = True
            return -2
        elif lineword == "BBW":
            self.was_last_left = True
            return -1
        elif lineword == "WBW":
            return 0
        elif lineword == "WBB":
            self.was_last_left = False
            return 1
        elif lineword == "WWB":
            self.was_last_left = False
            return 2
        else:
            return 0
        


if __name__ == "__main__":
    ultrasonic = UltraSonic()
    line_sensors = LineSensors()
    rosebot_adc = RosebotAdc()
    try:
        while True:
            distance = ultrasonic.get_cm()
            # print(f"Distance: {distance:.2f} cm")
            # print(f"Left Sensor: {line_sensors.get_left()}")
            # print(f"Line Sensors: {line_sensors.get_lineword()}  Value: {line_sensors.get_value()}")
            
            print(f"Left LDR: {rosebot_adc.get_left_photoresistor()}V, Right LDR: {rosebot_adc.get_right_photoresistor()}V, Battery Voltage: {rosebot_adc.get_battery_voltage()}V")
            
            time.sleep(2.0)
    except KeyboardInterrupt:
        print("Program terminated.")
        rosebot_adc.close()
        