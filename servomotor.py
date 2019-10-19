#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11,20)
p.start(0)

try:
    while True:
        p.ChangeDutyCycle(12.5)
        time.sleep(2)
        p.ChangeDutyCycle(2.5)
        time.sleep(2)
        p.ChangeDutyCycle(7.5)
        time.sleep(2)
except KeyboardInterupt:
    p.stop()
    GPIO.cleanup()
