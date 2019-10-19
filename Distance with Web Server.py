import RPi.GPIO as GPIO
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

HOST = "192.168.1.123"
PORT = 8088

GPIO.setmode(GPIO.BCM)

TRIG = 18 
ECHO = 23

print("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def getDist():
    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print("Distance:",distance,"cm")
    return distance

class MyHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        distance = str(getDist())
        outputString = "distance = " + distance

        self.wfile.write(outputString.encode("utf-8"))
        return

class ThreadedHTTPServer (ThreadingMixIn, HTTPServer):
    """Create a server thread to handle requests"""

if __name__ == "__main__":
    server_class = ThreadedHTTPServer
    httpd = server_class((HOST, PORT), MyHandler)

    try:
        print("Starting server")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("Stopping server")
        GPIO.cleanup()

