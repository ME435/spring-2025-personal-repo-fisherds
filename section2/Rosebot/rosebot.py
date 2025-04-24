from rosebot_drive_system import DriveSystem
from rosebot_sensors import Ultrasonic, LineSensors

class RoseBot:
    
    def __init__(self):
        self.drive_system = DriveSystem()
        self.ultrasonic = Ultrasonic()
        self.line_sensors = LineSensors()
        