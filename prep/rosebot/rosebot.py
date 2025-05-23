from rosebot_drive_system import DriveSystem
from rosebot_leds import CarLeds
from rosebot_servo_head import ServoHead
import rosebot_sensors
import gpiozero as gz


class RoseBot:
    
    def __init__(self):
        self.drive_system = DriveSystem()
        self.ultrasonic = rosebot_sensors.UltraSonic()
        self.line_sensors = rosebot_sensors.LineSensors()
        self.buzzer = gz.Buzzer(17)
        self.leds = CarLeds()
        self.servo_head = ServoHead()
        self.adc = rosebot_sensors.RosebotADC()

