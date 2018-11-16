#This is test code to sweep a servo
import sys
sys.path.append("..")
import RPi.GPIO as GPIO
import time as time
from robot.networking import RobotNetwork

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

servo = GPIO.PWM(18,500)
servo.start(0)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

network = RobotNetwork('http://10.135.79.80:8000/')

try:
    while True:
        webStatus = network.getControllerStatus()
        if (webStatus["a"] == 1):
            pwm.set_pwm(0, 0, 400)
        else:
            pwm.set_pwm(0, 0, 0)
except KeyboardInterrupt:
    pass

servo.stop()
GPIO.cleanup();