#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

outpin = 11
GPIO.setmode(GPIO.BOARD)

GPIO.setup(outpin, GPIO.OUT)

for i in range(0, 20):
    GPIO.output(outpin, GPIO.HIGH)
    #GPIO.output(outpin, True)
    #GPIO.output(outpin, 1)
    time.sleep(.3)
    GPIO.output(outpin, GPIO.LOW)
    #GPIO.output(outpin, False)
    #GPIO.output(outpin, 0)
    time.sleep(.3)
    
GPIO.cleanup()
