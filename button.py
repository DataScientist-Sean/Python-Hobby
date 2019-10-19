#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

outpin = 11
inpin = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(outpin, GPIO.OUT)
GPIO.setup(inpin, GPIO.IN)

def loop():
    if (GPIO.input(inpin) == True):
        print("button is up")
        GPIO.output(outpin, GPIO.HIGH)
        #GPIO.output(outpin, True)
        #GPIO.output(outpin, 1)
    else:
        GPIO.output(outpin, GPIO.LOW)
        #GPIO.output(outpin, False)
        #GPIO.output(outpin, 0)
        print("button is down")
    time.sleep(.3)
    

if __name__ == "__main__":
    try:
        print("Press Ctrl-C to quit.")
        while True:
            loop()
    except KeyboardInterrupt:
        print("shutting down")
    finally:
        GPIO.cleanup()











    

