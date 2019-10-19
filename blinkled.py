#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial = GPIO.HIGH)

for x in range(0,100):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(11, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
