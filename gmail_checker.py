#!/usr/bin/python3

import RPi.GPIO as GPIO

from imaplib import IMAP4_SSL as IMAP

import re, time

HOST = "imap.gmail.com"
USER = "oosddemo3@gmail.com"
PWD = "OOSDP@$$w0rd123"
FOLDER = "INBOX"

GPIO.setmode(GPIO.BOARD)
GREEN_LED = 11
RED_LED = 12

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def loop():
    server = IMAP(HOST, 993)
    server.login(USER, PWD)
    server.select(FOLDER, readonly=True)
    status,folder_status = server.status(FOLDER, "(UNSEEN)")
    print(status)
    print(folder_status)
    match = re.search("UNSEEN (\d+)", folder_status[0].decode(encoding="UTF-8"))
    print(match.group(0))
    print(match.group(1))
    if (match.group(1) == 1):
        print("You have mail!")
        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
    else:
        print("No unread mail")
        GPIO.output(GREEN_LED, False)
        GPIO.output(RED_LED, True)
        

if __name__ == "__main__":
    try:
        print("Press Ctrl-C to quit")
        while True:
            loop()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Shutting down")
    finally:
        GPIO.cleanup()









