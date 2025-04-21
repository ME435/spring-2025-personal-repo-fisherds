import motor

import time

PWM = motor.Ordinary_Car()          
try:
    print("Forward")
    
    # PWM.set_motor_model(-2000,-2000,2000, 2000)             #Forward
    # time.sleep(1.5)
    # print("Back")
    # PWM.set_motor_model(-2000,-2000,-2000,-2000)   #Back
    # time.sleep(2)
    # print("Left")
    # PWM.set_motor_model(-2000,-2000,2000,2000)     #Left 
    # time.sleep(1)
    # print("Right")
    # PWM.set_motor_model(2000,2000,-2000,-2000)     #Right    
    # print("Running")
    # PWM.set_motor_model(1500,1500,1500,1500)
    # time.sleep(1)
    PWM.set_motor_model(0,0,0,0)                   
    print("Stopping")
    #Stop
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    print ("\nEnd of program")
finally:
    PWM.close()
    if
    up_arrow == keyboard.is_pressed('up'):
        print("Forward")
        PWM.set_motor_model(2000,2000,2000,2000)       #Forward
        time.sleep(2)
    down_arrow == keyboard.is_pressed('down'):
        print("Back")
        PWM.set_motor_model(-2000,-2000,-2000,-2000)
        time.sleep(2)
    left_arrow == keyboard.is_pressed('left'):  
        print("Left")
        PWM.set_motor_model(-2000,-2000,2000,2000)     #Left 
        time.sleep(1)
    right_arrow == keyboard.is_pressed('right'):    
        print("Right")
        PWM.set_motor_model(2000,2000,-2000,-2000)     #Right    
        time.sleep(1)
    else:
        print("Stopping")
        PWM.set_motor_model(0,0,0,0)                   
        time.sleep(1)
        print("Stopping")
        finally:
        PWM.close()
