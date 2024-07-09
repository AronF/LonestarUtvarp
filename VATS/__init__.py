from .getdata import getData
from .cleanup import cleanup
from .led import ledOn, ledOff
from .fm import isFM
from .pindefs import *
import RPi.GPIO as gpio

#using board pin names
gpio.setmode(gpio.BOARD)

#set inputs and outputs
gpio.setup([DATA, CLOCK], gpio.IN)
gpio.setup(FMAM, gpio.IN, pull_up_down=gpio.PUD_UP)
#INTERRUPT is active low so it's initallized high
#light is off when LED is high (no current flowing from high to high)
gpio.setup([INTERRUPT, LED], gpio.OUT, initial=gpio.HIGH)

