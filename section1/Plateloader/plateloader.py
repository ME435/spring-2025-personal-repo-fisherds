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
        return "FAKE RESPONSE"
    
    
if __name__ == "__main__":
    print("Running a Plateloader test program")
    plateloader = Plateloader()
    plateloader.connect()
    while True:
        response = ""
        print("\n\n0. Exit")
        print("1. RESET")
        print("2. X-AXIS")
        selection = input("Select an option: ")
        if selection == "0":
            break
        elif selection == "1":
            response = plateloader.send_command("RESET")
        else:
            print("Invalid selection", selection)
        print("Response:", response)
    
    print("Goodbye!")
        