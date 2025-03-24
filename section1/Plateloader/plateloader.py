import serial
import time

class Plateloader:
    def __init__(self):
        self.is_connected = False
        self.ser = None
        
    def connect(self, port="/dev/cu.usbmodem11301"):
        self.ser = serial.Serial(port, baudrate=19200)
        print("Connecting... ", end="")
        while not self.ser.is_open:
            time.sleep(0.1)
        print("Connected!")
        time.sleep(1)
        self.ser.reset_input_buffer()
        self.is_connected = True
        
    def send_command(self, command):
        if not self.is_connected:
            self.connect()
        # Sending the message
        message_bytes = (command + "\n").encode()
        print("Sending:", message_bytes)
        self.ser.write(message_bytes)
        
        # Waiting for the response
        while self.ser.in_waiting == 0:
            time.sleep(0.1)
        while self.ser.in_waiting > 0:
            received = self.ser.readline()
            print("Received: ", received.decode().strip())
        return received
            
    
if __name__ == "__main__":
    print("Running a Plateloader test program")
    plateloader = Plateloader()
    plateloader.connect("/dev/ttyACM0")
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
        elif selection == "2":
            to_where = input("Enter the X-axis position: ")
            response = plateloader.send_command(f"X-AXIS {to_where}")
        else:
            print("Invalid selection", selection)
        print("Response:", response)
    
    print("Goodbye!")
        