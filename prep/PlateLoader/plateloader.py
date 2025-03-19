import time
import serial

class PlateLoader:
    def __init__(self, name="/dev/cu.usbmodem21101"):
        self.name = name
        self.is_connected = False
        self.ser = None
    
    def send_message(self, command):
        message_bytes = (command + "\n").encode()
        print(f"Sent     --> {message_bytes.decode().strip()}")
        self.ser.write(message_bytes)
        while self.ser.in_waiting == 0:
            time.sleep(0.1) # Avoids the self.ser.readline timeout
        while self.ser.in_waiting > 0:
            received = self.ser.readline()
            print("Received --> " + received.decode().strip())
        return received

    def connect(self):
        self.ser = serial.Serial(self.name, baudrate = 19200)
        print("Connecting… ", end="")
        while self.ser.is_open == False:
            time.sleep(0.1)
        print("Connected")
        time.sleep(1.0) # Important for some computers
        self.ser.reset_input_buffer()
        self.is_connected = True


if __name__ == "__main__":
    plateloader = PlateLoader()
    if plateloader.is_connected == False:
        plateloader.connect()
    while True:
        print("0: Exit")
        print("1: Reset")
        print("2: X-aix")
        print("3: Z-axis")
        print("4: Gripper")
        choice = input("Make a selection: ")
        resp = ""
        if choice == "0":
            break
        if choice == "1":
            resp = plateloader.send_message("RESET")
        if choice == "2":
            to_pos = input("Where to: ")
            resp = plateloader.send_message(f"X-AXIS {to_pos}")
        if choice == "3":
            z = input("Press 1 to Extend, 2 to Retract: ")
            if z == "1":
                resp = plateloader.send_message('Z-AXIS EXTEND')
            if z == "2":
                resp = plateloader.send_message('Z-AXIS RETRACT\n')
        print(resp)
    print("Goodbye")

