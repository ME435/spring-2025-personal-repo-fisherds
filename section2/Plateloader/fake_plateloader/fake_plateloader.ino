String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(19200);
  inputString.reserve(200);
}

void loop() {
  if (stringComplete) {

    if (inputString.equals("RESET")) {
      delay(1000);  // Simulated robot moving
      Serial.println("READY,  SAGIAN PE Loader, ROM Ver. 1.1.6, 12APR2001");
    } else if (inputString.startsWith("MOVE ")) {
      delay(3000);
      Serial.println("READY");
    } else if (inputString.equals("Z-AXIS EXTEND")) {
      Serial.println("READY, EXTENDED");
    } else if (inputString.equals("Z-AXIS RETRACT")) {
      Serial.println("READY, RETRACTED");
    } else if (inputString.startsWith("X-AXIS ")) {
      Serial.println("READY");
    } else if (inputString.equals("GRIPPER OPEN")) {
      Serial.println("READY, OPEN");
    } else if (inputString.equals("GRIPPER CLOSE")) {
      Serial.println("READY, CLOSED, NOPLATE");
    } else if (inputString.startsWith("SET_DELAY ")) {
      Serial.println("This feature is not supported on this fake plateloader");
    } else if (inputString.equals("LOADER_STATUS")) {
      Serial.println("READY, POSITION 3, Z-AXIS RETRACTED, GRIPPER CLOSED, NOPLATE");
    } else {
      Serial.print("Received Unknown command: ");
      Serial.println(inputString);
    }

    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}
