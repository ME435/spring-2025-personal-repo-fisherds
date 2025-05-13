from rosebot_drive_system import DriveSystem
from rosebot_sensors import UltraSonic, LineSensors, RosebotAdc
from rosebot_servo_head import ServoHead
import gpiozero as gz


class RoseBot:
    
    def __init__(self):
        self.drive_system = DriveSystem()
        self.ultrasonic = UltraSonic()
        self.line_sensors = LineSensors()
        self.servo_head = ServoHead()
        self.buzzer = gz.Buzzer(17)
        self.adc = RosebotAdc()
        