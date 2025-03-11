class PlateLoader:
    def __init__(self):
        self.is_connected = False
        self.ser = None # Serial port object
        
    def connect(self, port):
        self.is_connected = True
        # TODO: On Monday actually connect
        
    def send_command(self, command):
        if not self.is_connected:
            self.connect()
        # TODO: On Monday actually send command
        return "Fake response"


if __name__ == "__main__":
    print("Testing PlateLoader")
    plateloader = PlateLoader()
    plateloader.connect("/dev/cu.usbmodem1201")
    while True:
        resp = ""
        print("\n\n0. Exit")
        print("1. RESET")
        print("2. X-AXIS")
        selection = input("Make a selection: ")
        if selection == "0":
            break
        elif selection == "1":
            resp = plateloader.send_command("RESET")
        else:
            print("Invalid selection", selection)
        print("Response:", resp)
        
    print("Goodbye!")
    