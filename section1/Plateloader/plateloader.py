class Plateloader:
    def __init__(self):
        self.is_connected = False
        self.ser = None
        
    def connect(self, name="/dev/tty.usbmodem1201"):
        # TODO: Actually connect to the serial port
        self.is_connected = True
        
    def send_command(self, command):
        if not self.is_connected:
            self.connect()
        # TODO: Actually send the command and return the response
    
if __name__ == "__main__":
    print("Running a Plateloader test program")
        
        