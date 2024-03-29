#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#enable_pin = 18
coil_A_1_pin = 31
coil_A_2_pin = 33
coil_B_1_pin = 35
coil_B_2_pin = 37

#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

#GPIO.output(enable_pin, 1)


def forward(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(1, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)

def backwards(delay, steps):
    for i in range(0, steps):
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)


while True:
    setStep(0,0,0,0);
    delay = input("Delay between steps (milliseconds)?")
    steps = input("How many steps forward? ")
    forward(int(delay) / 1000.0, int(steps))
    steps = input("How many steps backwards? ")
    backwards(int(delay) / 1000.0, int(steps))
