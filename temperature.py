#!/usr/bin/python3

import os
import glob
import re
import time

os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")
base_dir = "/sys/bus/w1/devices/"

envvariables = os.environ
print(envvariables["PWD"])

folder = glob.glob(base_dir + "22-*")[0]
file = folder + "/w1_slave"

def loop():
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    
    match = re.search("t=(\d+)", lines[1])
    return str(float(match.group(1)) / 1000)

if __name__ == "__main__":
    print("Ctrl-C to exit")
    try:
        while True:
            print("Temperature=" + loop())
            time.sleep(.5)
    except KeyboardInterrupt:
        print("Shutting down")







