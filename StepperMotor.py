import RPi.GPIO as GPIO
from time import sleep

#max steps for the motor to turn
MAX_STEPS = 265

#set input pins 1,2,3,4
Pins = (5, 6, 13, 19)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Pins, GPIO.OUT)

#set all pins to LOW
GPIO.output(Pins, (GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW))

def o_lock():
        number_of_steps = 1

        #increment until the motor tuns to max number of steps
        while True:
            GPIO.output(Pins, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
            sleep(0.002)

            GPIO.output(Pins, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
            sleep(0.002)

            GPIO.output(Pins, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
            sleep(0.002)

            GPIO.output(Pins, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
            sleep(0.002)

            number_of_steps += 1

            #when max_steps is reached, set all pins to LOW
            if number_of_steps == MAX_STEPS:
                GPIO.output(Pins, (GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW))
                break

def c_lock():
        number_of_steps = 1

        #increment until the motor tuns to max number of steps
        while True:
            GPIO.output(Pins, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
            sleep(0.002)

            GPIO.output(Pins, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
            sleep(0.002)

            GPIO.output(Pins, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
            sleep(0.002)

            GPIO.output(Pins, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
            sleep(0.002)

            number_of_steps += 1

            #when max_steps is reached, set all pins to LOW
            if number_of_steps == MAX_STEPS:
                GPIO.output(Pins, (GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW))
                break