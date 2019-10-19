#!/usr/bin/python3

import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from socketserver import ThreadingMixIn

GPIO.setmode(GPIO.BOARD)
pinred = 12
pingreen = 16
pinblue = 18

GPIO.setup(pinred, GPIO.OUT)
GPIO.setup(pingreen, GPIO.OUT)
GPIO.setup(pinblue, GPIO.OUT)

class MyHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        query = str(self.path)
        color = query.split("=")[1]
        if (color=="red"):
            GPIO.output(pinred, True)
            GPIO.output(pingreen, False)
            GPIO.output(pinblue, False)
        elif (color=="green"):
            GPIO.output(pinred, False)
            GPIO.output(pingreen, True)
            GPIO.output(pinblue, False)
        elif (color=="blue"):
            GPIO.output(pinred, False)
            GPIO.output(pingreen, False)
            GPIO.output(pinblue, True)
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(("The LED is " + color).encode("utf-8"))
        return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """handle requests in a thread"""


if __name__ == "__main__":
    server_class = ThreadedHTTPServer
    httpd = server_class(("", 1080),MyHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Stopping server")
    GPIO.cleanup()





        
