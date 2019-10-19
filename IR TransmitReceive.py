#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
#GPIO.setup(11, GPIO.OUT)

def loop():
    if (GPIO.input(12) == True):
       print("IR is ON")
       #GPIO.output(11, 0)
    else:
       print("IR is OFF")
       #GPIO.output(11, 1)
    time.sleep(0.5)


if __name__ == "__main__":
    print("starting")
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        pass
    finally:
        print("shutting down")
        GPIO.cleanup()
