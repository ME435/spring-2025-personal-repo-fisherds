bool isStringComplete = false;
String inputString = "";

void setup() {
  Serial.begin(19200);
  pinMode(LED_BUILTIN, OUTPUT);
  inputString.reserve(200);
}

void loop() {
  if (isStringComplete) {
    if (inputString.equals("RESET")) {
      Serial.println("READY,  SAGIAN PE Loader, ROM Ver. 1.1.6, 12APR2001");
    } else if (inputString.startsWith("X-AXIS ")) {
      Serial.println("READY");
    } else if (inputString.startsWith("MOVE ")) {
      delay(3000);  // Simulated 3 seconds for the movement
      Serial.println("READY");
    } else if (inputString.equals("Z-AXIS EXTEND")) {
      Serial.println("READY, EXTENDED");
    } else if (inputString.equals("Z-AXIS RETRACT")) {
      Serial.println("READY, RETRACTED");
    } else if (inputString.equals("GRIPPER OPEN")) {
      Serial.println("READY, OPEN");
    } else if (inputString.equals("GRIPPER CLOSE")) {
      Serial.println("READY, CLOSED, NOPLATE");
    } else if (inputString.equals("LOADER_STATUS")) {
      Serial.println("READY, POSITION 3, Z-AXIS RETRACTED, GRIPPER CLOSED, NOPLATE");
    } else {
      Serial.print("Unknown command --> ");
      Serial.println(inputString);
    }
    inputString = "";
    isStringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char) Serial.read();
    if (inChar == '\n') {
      isStringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}
