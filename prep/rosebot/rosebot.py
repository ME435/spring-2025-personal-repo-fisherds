import rosebot_drive_system


class RoseBot:
    """ Container for all of the different robot submodules. The top level does nothing."""

    def __init__(self):
        self.drive_system = rosebot_drive_system.DriveSystem()
