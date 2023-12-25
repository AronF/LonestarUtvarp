from .getdata import getData
from .cleanup import cleanup
from .pindefs import *
import RPi.GPIO as gpio

#using board pin names
gpio.setmode(gpio.BOARD)

#set inputs and outputs
gpio.setup([DATA, CLOCK], gpio.IN)
#INTERRUPT is active low so it's initallized high
gpio.setup(INTERRUPT, gpio.OUT, initial=gpio.HIGH)
