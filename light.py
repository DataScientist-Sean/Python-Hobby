#!/usr/bin/python3

import time, spidev

spi = spidev.SpiDev()

spi.open(0, 0)
spi.max_speed_hz = 1350000

def loop():
    r = spi.xfer2([1,(8 + 0)<<4,0])
    return ((r[1]&3)<<8)+r[2]
    

if __name__ == "__main__":
    print("Ctrl-C to exit")
    try:
        while True:
            print("Light level=", loop())
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down")
