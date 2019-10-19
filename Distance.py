#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

trig = 12
echo = 16

GPIO.setmode(GPIO.BOARD)

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def loop():
    GPIO.output(trig, False)
    time.sleep(1)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0:
        pulse_start = time.time()
        
    while GPIO.input(echo) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("Distance: ", distance, "cm")
    return

if __name__ == "__main__":
    try:
        print("Press Ctrl-C to quit.")
        while True:
            loop()
    except KeyboardInterrupt:
        print("shutting down")
    finally:
        GPIO.cleanup()
