# Freenove Car and RoseBot Notes

Covers the three car lecture days between GPIO day and MQTT day. In 2025 those were Mon 4/21, Tue 4/22 and Thu 4/24. The sensor code (`rosebot_sensors.py`, sensor version of `rosebot.py`, `line_following.py`) is already in **"IR Line Following Sensors and Ultrasonic to Line Follow"** and isn't repeated here.

| Day | Topic | Copy in | Write live |
|---|---|---|---|
| 1 | Freenove code tour | Freenove zip | `params.json`, motor direction flip, small `test.py` edits |
| 2 | RoseBot drive system (Lab 4a) | `motor.py`, `pca9685.py` (from Day 1), `test_drive_system.py` (gist) | `rosebot.py`, `rosebot_drive_system.py`, TODOs in `test_drive_system.py` |
| 3 | Sensors (Lab 4b) | nothing new | `rosebot_sensors.py`, `set_speeds`, `line_following.py` skeleton |

---

# Day 1: Freenove Code (Chapters 3–6, Sensors and Actuators)

## Getting the code

1. Download https://github.com/Freenove/Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/archive/master.zip
2. Copy `Client/`, `Server/`, `setup.py` (and the mecanum tutorial PDF) into `sectionN/FreenoveCode/`.
3. On the Pi, work in `FreenoveCode/Server/`. Everything below runs from there.

## How to run the demos

`test.py` takes the device name as a command-line argument:

```
cd FreenoveCode/Server
python test.py Motor
python test.py Led
python test.py Ultrasonic
python test.py Infrared
python test.py Servo
python test.py ADC
python test.py Buzzer
```

Demo order in 2025: Motor first (to find wheel order and direction), then Led, then a quick look at Ultrasonic and Infrared. Those two come back on Day 3 through gpiozero.

`car.py` is a separate program (Freenove's autonomous modes). It is NOT what `test.py Motor` runs. In 2025 the only one demoed was **`python car.py Rotate`**. The others are listed for reference:

```
python car.py Rotate     # spins while translating, uses time_compensate (Change 3)
python car.py Sonic      # servo sweeps the ultrasonic sensor, obstacle avoidance
python car.py Infrared   # Freenove's line follower (preview of Lab 5b)
python car.py Light      # steer toward light with the photoresistors
```

`Car()` sets up the servo, ultrasonic, infrared and ADC, so every mode needs that hardware. All modes run until Ctrl+C.

Which files need what:
- `test.py Motor` uses only `motor.py` + `pca9685.py`. No `params.json` needed.
- `led.py` and `adc.py` read `params.json`. Run `python parameter.py` before `test.py Led`, `test.py ADC`, or any `car.py` mode.
- `car.py` uses `Ordinary_Car`, so do the motor flip (Change 2) first or everything drives backward.

Step 0 (fresh Pi images): enable I2C and SPI. Without I2C, `python test.py Motor` crashes at `smbus.SMBus(1)` with `FileNotFoundError: [Errno 2] No such file or directory`, because `/dev/i2c-1` doesn't exist yet.

```
sudo raspi-config nonint do_i2c 0   # 0 = enable
sudo raspi-config nonint do_spi 0   # LEDs use SPI (GPIO 10)
ls /dev/i2c* /dev/spidev*           # expect /dev/i2c-1 and /dev/spidev0.0 (reboot if missing)
i2cdetect -y 1                      # optional: expect 40 (PCA9685) and 48 (ADC)
```

Suggested Day 1 order:
1. Copy in the Freenove code, `cd Server`
2. `python test.py Motor`: everything runs backward
3. Flip the duties in `motor.py` (Change 2), rerun
4. One wheel at a time in `test_Motor` (Change 5) to match duty1–4 to fl, rl, fr, rr
5. `python parameter.py` (enter 2, 2)
6. Comment out the `rpi_ledpixel` import in `led.py` (Change 4), then `python test.py Led`, then Ultrasonic, Infrared, Servo, Buzzer, ADC
7. Demo `python car.py Rotate` and tune `time_compensate` (Change 3)

## Change 1: params.json (new file)

The Freenove code reads `params.json` to choose the hardware version, which decides things like SPI vs. GPIO 18 for the LEDs. Running `python parameter.py` creates it: it asks for Connect Version (enter 2) and PCB Version (enter 2) and detects the Pi version itself (1 = less than Pi 5). In 2025 we wrote it by hand, which works too:

params.json
```json
{
    "Connect_Version": 2,
    "Pcb_Version": 2,
    "Pi_Version": 1
}
```

## Change 2: motor.py: flip all four motor directions

Our motors spin the opposite way from Freenove's defaults, so "forward" drove backward. The fix negates every duty in `set_motor_model`.

motor.py (inside class `Ordinary_Car`)
```python
    def set_motor_model(self, duty1, duty2, duty3, duty4):
        duty1,duty2,duty3,duty4=self.duty_range(duty1,duty2,duty3,duty4)
        self.left_upper_wheel(-duty1)    # was duty1
        self.left_lower_wheel(-duty2)    # was duty2
        self.right_upper_wheel(-duty3)   # was duty3
        self.right_lower_wheel(-duty4)   # was duty4
```

Talking points:
- Duty order is **front left, rear left, front right, rear right** (fl, rl, fr, rr). This is the duty1–duty4 table on Quiz 17.
- Duty range is −4095 to 4095 (PCA9685 is 12-bit). `duty_range` clamps it.

## Change 3: car.py: time_compensate

Only matters for Freenove's own rotation mode. Tune it per car.

car.py (in `Car.__init__`)
```python
        self.time_compensate = 1.6   # was 3. Section 2 used 1.8.
```

## Change 4: led.py: use the SPI LED strip

With `Connect_Version: 2` and a Pi older than the Pi 5, `Led` uses `Freenove_SPI_LedPixel` (GPIO 10 / SPI). **Commenting out the `rpi_ledpixel` import is REQUIRED.** Without it, `python test.py Led` crashes with `ModuleNotFoundError: No module named 'rpi_ws281x'`, even though that GPIO 18 branch is never used (it only runs when `Connect_Version == 1`). In 2025 Section 1's copy of this change just never got committed.

led.py
```python
# from rpi_ledpixel import Freenove_RPI_WS281X  # Pin 18 approach - fails anyway
from spi_ledpixel import Freenove_SPI_LedPixel  # SPI GPIO10 approach that works!
```

## Change 5: test.py: one wheel at a time, and blinking LEDs

**Motor:** comment out their forward/back/left/right sequence and spin ONE wheel to discover which duty is which wheel and which sign is forward. Students can change the arguments and rerun.

test.py (in `test_Motor`)
```python
    try:
        PWM.set_motor_model(0, -1000, 0, 0)   # Try one wheel at a time
        time.sleep(3)
        # PWM.set_motor_model(1000,1000,1000,1000)         #Forward
        # ... (rest of their sequence commented out)
        PWM.set_motor_model(0,0,0,0)                     #Stop
```

**LED:** `ledIndex(mask, r, g, b)` uses a **bitmask** (0x01, 0x02, 0x04 … 0x80) for the 8 LEDs, and `colorBlink(0)` turns them all off.

test.py (in `test_Led`)
```python
    try:
        for k in range(8):
            led.ledIndex(0x01, 255, 0, 0)
            led.ledIndex(0x02, 255, 0, 0)
            led.ledIndex(0x04, 255, 0, 0)
            led.ledIndex(0x08, 255, 0, 0)
            led.ledIndex(0x10, 255, 0, 0)
            led.ledIndex(0x20, 255, 0, 0)
            led.ledIndex(0x40, 255, 0, 0)
            led.ledIndex(0x80, 255, 0, 0)
            time.sleep(0.5)
            led.colorBlink(0)   # turn off the lights
            time.sleep(0.5)

            # Freenove's original rainbow, commented out (easy to switch back)
            # led.ledIndex(0x01, 255,   0,   0)      #Red
            # led.ledIndex(0x02, 255, 125,   0)      #orange
            # led.ledIndex(0x04, 255, 255,   0)      #yellow
            # led.ledIndex(0x08,   0, 255,   0)      #green
            # led.ledIndex(0x10,   0, 255, 255)      #cyan-blue
            # led.ledIndex(0x20,   0,   0, 255)      #blue
            # led.ledIndex(0x40, 128,   0, 128)      #purple
            # led.ledIndex(0x80, 255, 255, 255)      #white
```

That's the 2025 Section 2 version. Section 1 ran Freenove's rainbow unchanged and only added prints (`"LED test program is starting ..."` in `test.py`, `"Using SPI LED strip"` in `led.py`) to show the SPI path was used. `led.py` also has `rainbowCycle()`, `rainbowbreathing()` and `following()` for flashier demos.

---

# Day 2: RoseBot Drive System (SSH Car, Lab 4a)

## Where the starting code comes from

From the "SSH Car" slide deck ("Starting code" slide): students create three files in their `Rosebot/` folder: `rosebot_drive_system.py`, `rosebot.py`, `test_drive_system.py`.

| File | Source |
|---|---|
| `test_drive_system.py` | **The gist** (the only starter code handed out): https://gist.github.com/fisherds/c4ca6a6fc653a6033b236a7c256ab165 |
| `motor.py` | Copied from their Day 1 `FreenoveCode/Server`. Rename class `Ordinary_Car` → `OrdinaryCar` and keep the four negated duties. |
| `pca9685.py` | Copied unchanged from `FreenoveCode/Server` (`motor.py` imports it). |
| `rosebot.py`, `rosebot_drive_system.py` | Start EMPTY. Written live, following the "RoseBot planning" diagram slide (robot → drive_system → car → duty1–4) and the "DriveSystem potential methods" slide. |

The gist is a TODO-driven harness. Students un-comment one `run_test_...` at a time in `run_test_drive_system()`, then fill in its TODO. The gist's TODOs:

1. Put your name in the docstring.
2. Construct the robot. The gist has `robot = None` and **no import**, so students add `import rosebot` and `robot = rosebot.RoseBot()`.
3. `run_test_go_stop`
4. `run_test_go_straight_for_seconds`
5. `run_test_go_straight_for_inches`
6. `run_test_spin_in_place_for_seconds`
7. `run_test_spin_in_place_for_degrees`
8. `run_test_draw_polygon` (left for Lab 4a)

## rosebot.py: first thing written live

```python
from rosebot_drive_system import DriveSystem

class RoseBot:
    
    def __init__(self):
        self.drive_system = DriveSystem()
```

## rosebot_drive_system.py: first version (just enough for TODO 3)

```python
from motor import OrdinaryCar

class DriveSystem:
    
    def __init__(self):
        self.car = OrdinaryCar()
    
    def go(self, left_speed, right_speed):
        print("TODO: Use self.car to GO")
    
    def stop(self):
        print("TODO: Use self.car to STOP")
```

## rosebot_drive_system.py: written in class

Order written: `scale_speed` → `go`/`stop`/`close` → `go_straight_for_seconds` → `strafe_left`/`strafe_right` → `go_straight_for_inches` → `spin_in_place_for_seconds` → `spin_in_place_for_degrees`. Then `move_in_direction` and `strafe_circle` were pasted in from prep as a "look what mecanum can do" demo. `set_speeds` was added on Day 3 for line following.

rosebot_drive_system.py
```python
from motor import OrdinaryCar
import time
import math

class DriveSystem:
    
    def __init__(self):
        self.car = OrdinaryCar()
        
    def scale_speed(self, speed):
        """ Converts -100 to 100 into a -4095 to 4095 duty. """
        return int(speed / 100 * 4095)

    def set_speeds(self, lf_speed, lr_speed, rf_speed, rr_speed):
        """ Day 3 addition: set all four wheels (used by line_following.py). """
        self.car.set_motor_model(self.scale_speed(lf_speed), self.scale_speed(lr_speed),
                                 self.scale_speed(rf_speed), self.scale_speed(rr_speed))
    
    def go(self, left_speed, right_speed):
        left_duty = self.scale_speed(left_speed)
        right_duty = self.scale_speed(right_speed)
        self.car.set_motor_model(left_duty, left_duty, right_duty, right_duty)

    def stop(self):
        self.car.set_motor_model(0, 0, 0, 0)
    
    def close(self):
        self.car.close()
    
    def go_straight_for_seconds(self, seconds, speed):
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()
        
    def strafe_left(self, speed):
        duty = self.scale_speed(speed)
        self.car.set_motor_model(-duty, duty, duty, -duty)
        
    def strafe_right(self, speed):
        self.strafe_left(-speed)

    def go_straight_for_inches(self, inches, speed):
        # TODO in Lab 4A run some experiment using go_straight_for_seconds to guess a good m and B
        m = 0.2
        B = 0
        inches_per_second = m * speed + B
        seconds = inches / inches_per_second
        self.go_straight_for_seconds(seconds, speed)

    def spin_in_place_for_seconds(self, seconds, speed, isLeft=True):
        duty = self.scale_speed(speed)
        if isLeft:
            self.car.set_motor_model(-duty, -duty, duty, duty)
        else:
            self.car.set_motor_model(duty, duty, -duty, -duty)
        time.sleep(seconds)
        self.stop()
        
    def spin_in_place_for_degrees(self, degrees, speed, isLeft=True):
        # TODO in Lab 4A run some experiment using spin_in_place_for_seconds to guess a good m and B
        m = 7
        B = 0
        degrees_per_second = m * speed + B
        seconds = degrees / degrees_per_second
        self.spin_in_place_for_seconds(seconds, speed, isLeft)

    def move_in_direction(self, speed, angle_in_degrees):
        # Front           Front
        #  Left           Right
        #    \             /
        #     \           /
        #      \         /
        #      [ROBOT BASE]
        #      /         \
        #     /           \
        #    /             \
        # Rear           Rear
        # Left           Right
        angle_rad = math.radians(angle_in_degrees)

        fl = math.sin(angle_rad + math.pi / 4)
        fr = -math.sin(angle_rad - math.pi / 4)
        rl = -math.sin(angle_rad - math.pi / 4)
        rr = math.sin(angle_rad + math.pi / 4)

        # Normalize to keep the maximum magnitude at 1.0
        max_val = max(abs(fl), abs(fr), abs(rl), abs(rr))
        fl = fl / max_val * speed
        fr = fr / max_val * speed
        rl = rl / max_val * speed
        rr = rr / max_val * speed

        self.car.set_motor_model(self.scale_speed(fl), self.scale_speed(rl),
                                 self.scale_speed(fr), self.scale_speed(rr))

    def strafe_circle(self, speed, duration_seconds):
        steps = 100  # More steps = smoother circle
        angle_step = 360 / steps
        delay = duration_seconds / steps
        for i in range(steps):
            angle = i * angle_step
            self.move_in_direction(speed, angle)
            time.sleep(delay)
        self.stop()


if __name__ == '__main__':
    drive_system = DriveSystem()
    try:
        # drive_system.go_straight_for_seconds(2, 50)
        # drive_system.strafe_left(50)
        # time.sleep(1)
        # drive_system.strafe_right(50)
        # time.sleep(1)
        # drive_system.spin_in_place_for_seconds(2, 50, True)
        # drive_system.spin_in_place_for_seconds(2, 50, False)
        # drive_system.move_in_direction(50, 45)
        # time.sleep(2)
        drive_system.strafe_circle(50, 5)
    finally:
        drive_system.close()
```

Talking points:
- Strafe pattern `(-d, d, d, -d)` and spin pattern `(-d, -d, d, d)` connect straight back to the mecanum force diagrams on Quiz 17.
- The `m * speed + B` placeholders are where Lab 4a starts: run `go_straight_for_seconds` / `spin_in_place_for_seconds` at a few speeds, measure, and fit m and B.
- Watch out: the 2025 Section 1 copy had `seconds = inches / degrees_per_second` in `spin_in_place_for_degrees`. It should be `degrees`.

## test_drive_system.py: TODOs filled in during class

Only the filled-in parts are shown. Each test also got a `robot.drive_system.close()` after its `while` loop.

TODO 2: construct the robot (top of file + in run_test_drive_system)
```python
import rosebot
# ...
    robot = rosebot.RoseBot()
```

TODO 3: run_test_go_stop
```python
        robot.drive_system.go(left_wheel_speed, right_wheel_speed)
        time.sleep(3)
        robot.drive_system.stop()
        print("The robot should have stopped moving.")
    
    robot.drive_system.close()
```

TODO 4: run_test_go_straight_for_seconds
```python
        robot.drive_system.go_straight_for_seconds(seconds, speed)
        print("The robot should have stopped moving.")
```

Side demo: in 2025 both sections temporarily used this test to try strafing (Section 2) and `move_in_direction` (Section 1):
```python
        left_right = input("Enter 'L' for strafe left, 'R' for strafe right: ")
        is_left = left_right == 'L'
        # ...
        if is_left:
            robot.drive_system.strafe_left(speed)
        else:
            robot.drive_system.strafe_right(speed)
        time.sleep(seconds)
        robot.drive_system.stop()

        # Section 1 version
        direction = float(input("Direction (e.g., 90): "))
        robot.drive_system.move_in_direction(speed, direction)
        time.sleep(seconds)
        robot.drive_system.stop()
```

TODO 5: run_test_go_straight_for_inches
```python
        robot.drive_system.go_straight_for_inches(inches, speed)
```

TODO 6: run_test_spin_in_place_for_seconds
```python
        robot.drive_system.spin_in_place_for_seconds(seconds, speed)  # Default is left CCW
```

TODO 7: run_test_spin_in_place_for_degrees
```python
        robot.drive_system.spin_in_place_for_degrees(degrees, speed)  # Default is left CCW
```

**Left for Lab 4a:** gist TODO 8, `run_test_draw_polygon`, which loops `spin_in_place_for_degrees` + `go_straight_for_inches`.

**Handout is stale:** the gist has no `turn_for_*` tests, but the Lab 4a handout still lists `run_test_turn_for_seconds`, `run_test_turn_for_degrees` and the `turn_for_seconds` / `turn_for_degrees` methods. It also marks the spin methods "optional", even though draw polygon needs `spin_in_place_for_degrees`. Update the handout to match the gist. Also fix the gist's `run_test_draw_polygon` docstring, which still says "turn_for_degrees".

---

# Day 3: Sensors (Quiz 18, Lab 4b)

The sensor code itself is in the **"IR Line Following Sensors and Ultrasonic to Line Follow"** notes. Missing from those notes:

## 1. set_speeds in rosebot_drive_system.py

`line_following.py` calls `robot.drive_system.set_speeds(lf, lr, rf, rr)`, which isn't part of the Day 2 code. Add this to `DriveSystem` (already included in the Day 2 listing above):

```python
    def set_speeds(self, lf_speed, lr_speed, rf_speed, rr_speed):
        self.car.set_motor_model(self.scale_speed(lf_speed), self.scale_speed(lr_speed),
                                 self.scale_speed(rf_speed), self.scale_speed(rr_speed))
```

## 2. line_following.py starter (what students get for Lab 4b)

In class we only wrote the skeleton. Students fill in the loop for Lab 4b.

line_following.py (starter)
```python
from rosebot import RoseBot
import time

def main():
    print("Line Follower")
    robot = RoseBot()
    
    try:
        while True:
            # Get the ultrasonic sensor reading
            # If the distance is less than 20 cm
            #   stop the robot
            # If the distance is greater than 20 cm, follow the line
            #   Get the line sensor readings
            #   Update the robot's speed based on the line sensor readings
            time.sleep(0.1)
    except KeyboardInterrupt:  # Handle keyboard interrupt (Ctrl+C)
        robot.drive_system.stop()
        robot.drive_system.close()
        print("\nEnd of program")
        
main()
```

## 3. Testing the sensors alone

`rosebot_sensors.py` has a `main()` for local testing. Run it directly before trying the line follower:

```
python rosebot_sensors.py
```

## 4. Names drifted between versions

Pick one set and use it everywhere:

| Sensor notes PDF | 2025 Section 2 in class |
|---|---|
| `UltraSonic` | `Ultrasonic` |
| `get_line_word()` | `get_lineword()` |
| `get_line_value()` | `get_value()` |
| `was_left_side` | `was_line_left` |
| `get_cm()` rounds to 0.1 | no rounding |
| has `is_line()` | — |

Pins (from Quiz 18): ultrasonic `trigger=27, echo=22`; line sensors left 14, middle 15, right 23.
