import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
motor_in1 = 2 #purple
motor_in2 = 3 #blue
motor_en  = 4 #green

GPIO.setup(motor_in1, GPIO.OUT)
GPIO.setup(motor_in2, GPIO.OUT)
GPIO.setup(motor_en, GPIO.OUT)

pwm=GPIO.PWM(motor_en, 100)

pwm.start(0)
GPIO.output(motor_in1, True)
GPIO.output(motor_in2, False)

pwm.ChangeDutyCycle(50)

sleep(2)
GPIO.output(motor_in1, False)
GPIO.output(motor_in2, True)

sleep(2)
pwm.stop()
GPIO.cleanup()
