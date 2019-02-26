"""
    File that will hold the source code for hardware that will be controlled by the Pi.
    All of the servos, motors, sensors, LEDs, etc. will be here.
"""
import RPi.GPIO as GPIO
import Adafruit_PCA9685

GPIO.setmode(GPIO.BOARD)

class Component:
    def __init__(self, controllerInput):
        #Make sure that everything has an init method
        raise NotImplementedError()

    def doUpdate(self, value):
        #Make sure everything has a method that can be called by the main method
        raise NotImplementedError()

class SensorComponent(Component):
    def __init__(self, name, channel):
        self.name = name
        self.channel = channel

    def __del__(self):
        #Don't know if we will use anything here
        pass

    def getSensorValues(self):
        #Get sensor values from robot asynchronously and return them in some data type
        pass

    def doUpdate(self, value):
        return self.getSensorValues()

class MotorComponent():
    def __init__(self, name, controllerInput, backwardInput, directionPin, pwmPin):
        GPIO.setmode(GPIO.BOARD)
        self.name = name
        self.controllerInput = controllerInput
        self.backwardInput = backwardInput
        self.directionPin = directionPin
        self.pwmPin = pwmPin
        self.motorPower = 0

        GPIO.setup(self.directionPin, GPIO.OUT)
        print(self.pwmPin)
        GPIO.setup(self.pwmPin, GPIO.OUT)
        GPIO.output(self.directionPin, False)

        self.PWM = GPIO.PWM(self.pwmPin, 1000) #set PWM to 1000 Hz as a max frequency
        self.PWM.start(0)
        self.PWM.ChangeDutyCycle(0)

    def __del__(self):
        #Make sure robot stops moving
        #self.updateSpeed(0)
        pass

    def updateSpeed(self, value):
        #Update motor speed
        if (value < 0):
            #Motor going in reverse
            GPIO.output(self.directionPin, False)
            pwm = -int(value)
            if (pwm > 100):
                pwm = 100
        elif (value > 0):
            #Motor going forwards
            GPIO.output(self.directionPin, True)
            pwm = int(value)
            if (pwm > 100):
                pwm = 100
        else:
            GPIO.output(self.directionPin, False)
            pwm = 0
        self.motorPower = pwm
        self.PWM.ChangeDutyCycle(pwm)
        pass

    def doUpdate(self, value, doBackwards):
        #This is the method we will call from the main loop when parsing controller data
        value *= (100/8191) #This translates the trigger range of 0 to 8191 into the pwm range of 0 to 100
        if (doBackwards == 1):
            value *= -1
        if ('left' in self.name):
            self.updateSpeed(-1 * value)
        elif ('right' in self.name):
            self.updateSpeed(value)
        else:
            pass

class ServoComponent(Component):
    def __init__(self, name, controllerInput, channel, homePosition, minValue, maxValue):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)
        self.name = name
        self.controllerInput = controllerInput
        self.channel = channel
        self.homePosition = homePosition
        self.minValue = minValue
        self.maxValue = maxValue

    def __del__(self):
        #Make servo return to some predefined "home" position
        self.updatePosition(self.homePosition)
        pass

    def updatePosition(self, value):
        #Update servo position
        if (value >= self.minValue and value <= self.maxValue):
            self.pwm.set_pwm(self.channel, 0, value)
            return True
        else:
            return False
    
    def doUpdate(self, value):
        #Method called from main loop when parsing data
        return self.updatePosition(value)

class LauncherServoComponent(Component):
    def __init__(self, name, channel, controllerInput):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.name = name
        self.channel = channel
        self.controllerInput = controllerInput

    def __del__(self):
        pass

    def updatePosition(self, value):
        if (value == 0): #MAKE THIS WHERE IT STOPS MOVING
            pass
        else: #MAKE THIS WHERE IT IS MOVING
            pass
        return True

    def doUpdate(self, value):
        return self.updatePosition(value)


class LEDComponent(Component):
    def __init__(self, name, controllerInput):
        self.name = name
        self.controllerInput = controllerInput
        self.currentValue = 0

    def __del__(self):
        #Make sure lights are turned off
        pass

    def updateValue(self, value):
        #Update LED value based on value and self.currentValue
        pass

    def doUpdate(self, value):
        #Method that is called from the main loop when parsing controller data
        pass