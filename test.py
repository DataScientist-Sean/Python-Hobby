#!/usr/bin/python

import time, spidev

spi = spidev.SpiDev()

# open spidev object on bus 0, device 0
spi.open(0,0)

# GPIO SPI pin setting:
# Clock = pin 23 (CLK)
# Chip Select = pin 24 (CE0)
# MISO (Master-In, Slave-Out) = pin 21
# MOSI (Master-Out, Slave-In) = pin 19

# No need to set the GPIO pins as spidev sets to these pins automatically

# MCP3008 Interaction:
#   We operate the chip by bringing the Chip Select pin to a LOW value
#   to put it into operating mode, and then causing clock-cycles by turning
#   the clock pin on and off (set the clock pin to High, then Low). The
#   clock causes the chip to send or receive one bit on the "down-side" of
#   the cycle. When we are done, we turn the CS pin to HIGH, which deactivates it.
#   If we are using the "bit-banging" technique, we send 5 bytes to the
#   chip and receive 12 back -- the first 2 are an empty bit and a null bit,
#   followed by 10 bits of data.
#   
#   If we are using the SPI pins on the Pi, and interacting through the
#   spidev methods, we don't need to set up the GPIO pins, as spidev does it
#   automatically, so we have to use the SPI pins on the GPIO bus
#   (19, 21, 23, and 24). We also don't have to manage the CS and Clock pins because
#   spidev does this for us when we call the xfer method. SPI can only communicate
#   in 8-bit bytes, so the xfer methods receive an array of bytes returned from
#   interacting with the chip.
#   The first byte is ignored. The second byte has the first 2 bits of the 10-bit result.
#   The third byte has the remaining 8 data bits.
#   SPI ends the communication cycle by switching the CS pin to HIGH.

def read_sensor():
    # using xfer2 method, sends data to chip, receives result in an array
    r = spi.xfer2([1,(8 + 0)<<4, 0])
    print((8 + 0)<<4)
    # passing one argument with 3 data items to chip. The data makes up 3 bytes,
    # so the binary value is 00000001, 10000000, and 00000000.
    # first value is the start-bit of 1
    # second value is the single-ended/differential mode bit, plus channel (0)
    # which is 8 (1000) plus 0 (0000) in this case, left-shifted 4 bits to give 128 (10000000)
    # The third value is 0, which is the dummy bit that would be on the start of the
    # next communication cycle, but included here to make processing the return value
    # simpler.
    
    adcout = ((r[1]&3)<<8)+r[2]
    # The MCP3008 produces 10-bit output.
    # xfer2 returned an array of bytes. We need to capture the last 2 bits of the
    # second byte and combine that with the entire third byte to get our
    # 10-bits of data by using a bitwise & with a value of 3 to zero-out the first 6 bits.
    # Then we shift the bits left by 8 bits, effectively multiplying by 2 to the 8th power,
    # and add the remaining 8 bits to the value.
    print("r=",r)
    print("r[0]=",r[0])
    print("r[1]=",r[1])
    print("r[2]=",r[2])
    print("(r[1]&3)<<8=",(r[1]&3)<<8)

    return adcout

while (True):
    print("result:", read_sensor())
