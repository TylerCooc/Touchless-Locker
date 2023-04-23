import RPi.GPIO as GPIO
from time import sleep

#set pin 37 for the relay Pin
relayPin = (26)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

#set relay pins to LOW
GPIO.output(relayPin, (GPIO.LOW))

def lightsOn():
    #turn on light
    GPIO.output(relayPin, (GPIO.HIGH))

    #wait for 900s = 15min
    #sleep(900)
    sleep(5)

    #turn light off
    GPIO.output(relayPin, (GPIO.LOW))