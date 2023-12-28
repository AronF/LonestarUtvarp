import RPi.GPIO as gpio
from .pindefs import *

#reads from the adc module returning a tuple of both read results
#reads LSB first (!!)
def getData():
    #interrupt low starts the communication with the chip
    gpio.output(INTERRUPT, 0)
    data = 0
    for i in range(16):
        #busy wait for the clock to go high
        while not gpio.input(CLOCK): pass
        #shift and add to the output
        bit = gpio.input(DATA) << i
        data |= bit
        #busy wait for the clock to go low again
        while gpio.input(CLOCK): pass
    #reset the interrupt for next time
    gpio.output(INTERRUPT, 1)
    return decode(data)

#helper function to split the 16 bit number into a tuple of 8 bit values
def decode(bytes):
    upper = bytes >> 8
    lower = bytes & 0x00FF
    return (upper, lower)
