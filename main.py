from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO
import cwiid

# blue tooth connect to wii remote

print('Press and hold the 1+2 butttons on your Wiimote simulatenously')
while True:
    try:
        wii=cwiid.Wiimote()
    except:
        print('re-attempting connection')
        continue
    else:
        print('connection established')
        break

wii.rpt_mode = cwiid.RPT_BTN

# initialize

print('initialize')

servo = Servo(5)
GPIO.setmode(GPIO.BCM)
motor_in1 = 2 #purple
motor_in2 = 3 #blue
motor_en  = 4 #green
GPIO.setup(motor_in1, GPIO.OUT)
GPIO.setup(motor_in2, GPIO.OUT)
GPIO.setup(motor_en, GPIO.OUT)
pwm=GPIO.PWM(motor_en, 100)
pwm.start(0)
pwm.ChangeDutyCycle(50)

# main loop

while True:
  buttons=wii.state["buttons"]
  if (buttons & cwiid.BTN_LEFT):
     servo.value=-0.5
  if (buttons & cwiid.BTN_RIGHT):
     servo.value=+0.5
  if (buttons & cwiid.BTN_UP):
     GPIO.output(motor_in1, True)
     GPIO.output(motor_in2, False)

  if (buttons & cwiid.BTN_DOWN):
     GPIO.output(motor_in1, False)
     GPIO.output(motor_in2, True)
  if (buttons & cwiid.BTN_B):
      GPIO.output(motor_in1, False)
      GPIO.output(motor_in2, False)
  if (buttons & cwiid.BTN_A):
     servo.value=-0
# ---------------------------

#try:
    #while True:

for x in range(0, -5, -1):
    servo.value=x/10
    sleep(0.2)
for x in range(-4, +5, +1):
    servo.value=x/10
    sleep(0.2)
for x in range(+4, 0, -1):
    servo.value=x/10
    sleep(0.2)
    
sleep(1.0)
servo.value=-0.1
sleep(1.0)
servo.value=-0.2
sleep(1.0)
servo.value=-0.3
sleep(1.0)
servo.value=-0.4
sleep(1.0)
servo.value=-0.5
sleep(1.0)
servo.value=-0.4
sleep(1.0)
servo.value=-0.3
sleep(1.0)
servo.value=-0.2
sleep(1.0)
servo.value=-0.1
sleep(1.0)
servo.value=-0
sleep(1.0)
servo.value=+0
sleep(1.0)
servo.value=+0.1
sleep(1.0)
servo.value=+0.2
sleep(1.0)
servo.value=+0.3
sleep(1.0)
servo.value=+0.4
sleep(1.0)
servo.value=+0.5
sleep(1.0)
servo.value=+0.4
sleep(1.0)
servo.value=+0.3
sleep(1.0)
servo.value=+0.2
sleep(1.0)
servo.value=+0.1
sleep(1.0)
servo.value=+0
sleep(1.0)
        #servo.value=-0.77
        #sleep(1.0)
        #servo.value=-1
        #sleep(1.0)
        #servo.value=-0.77
        #sleep(1.0)
        #servo.value=-0.60
        #sleep(1.0)
        #servo.value=-0.50
        #sleep(1.0)
        #servo.value=-0.30
        #sleep(1.0)
        #servo.value=-0.50
        #sleep(1.0)
        #servo.value=-0.60
        #sleep(1.0)
        #servo.value=-0.77
        #sleep(1.0)
        #servo.value=-0.60
        #sleep(1.0)
        #servo.value=-0.77
        #sleep(1.0)

        
       
        #pwm.ChangeDutyCycle(50)

        #sleep(2)
        
        #servo.value=-0.60
        #sleep(1.0)
        #servo.mid()
        #sleep(0.5)
        #servo.value=+0.3
        #sleep(0.5)
    	
#except KeyboardInterrupt:
   # print("Program stopped")

pwm.stop()
GPIO.cleanup()
