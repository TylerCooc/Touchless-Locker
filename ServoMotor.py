#!/usr/bin/python3
import RPi.GPIO as GPIO
import pigpio
import time

servo = 18 

# more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwmOpen = pigpio.pi()

pwm.set_PWM_frequency( servo, 50 )
pwmOpen.set_PWM_frequency( servo, 20)

def ServoMotorClose():
    #0 deg
    pwm.set_servo_pulsewidth( servo, 500 )
    time.sleep( 1 )
    pwm.set_PWM_dutycycle( servo, 0 )
    pwm.set_PWM_frequency( servo, 0 )

def ServoMotorOpen():
    #90 deg
    pwmOpen.set_servo_pulsewidth( servo, 2000 )
    time.sleep( 1 )
    pwmOpen.set_PWM_dutycycle( servo, 0 )
    pwmOpen.set_PWM_frequency( servo, 0 )