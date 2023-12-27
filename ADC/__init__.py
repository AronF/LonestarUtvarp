from .getdata import getData
from .cleanup import cleanup
from .led import ledOn, ledOff
from .am import isAM
from .pindefs import *
import RPi.GPIO as gpio

#using board pin names
gpio.setmode(gpio.BOARD)

#set inputs and outputs
gpio.setup([DATA, CLOCK, FMAM], gpio.IN)
#INTERRUPT is active low so it's initallized high
#light is off when LED is high (no current flowing from high to high)
gpio.setup([INTERRUPT, LED], gpio.OUT, initial=gpio.HIGH)

