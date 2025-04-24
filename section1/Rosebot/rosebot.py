from rosebot_drive_system import DriveSystem
from rosebot_sensors import UltraSonic, LineSensors

class RoseBot:
    
    def __init__(self):
        self.drive_system = DriveSystem()
        self.ultrasonic = UltraSonic()
        self.line_sensors = LineSensors()
        