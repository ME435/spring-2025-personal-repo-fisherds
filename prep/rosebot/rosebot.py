from rosebot_drive_system import DriveSystem
import rosebot_sensors

class RoseBot:
    
    def __init__(self):
        self.drive_system = DriveSystem()
        self.ultrasonic = rosebot_sensors.UltraSonic()
        self.line_sensors = rosebot_sensors.LineSensors()

