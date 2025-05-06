from rosebot_drive_system import DriveSystem
from rosebot_sensors import Ultrasonic, LineSensors
from rosebot_servo_head import ServoHead
import gpiozero as gz

class RoseBot:
    
    def __init__(self):
        self.drive_system = DriveSystem()
        self.ultrasonic = Ultrasonic()
        self.line_sensors = LineSensors()
        self.servo_head = ServoHead()
        self.buzzer = gz.Buzzer(17)
        