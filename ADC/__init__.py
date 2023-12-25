from .getdata import getData
from .cleanup import cleanup
from .pindefs import *
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

DATA = 11
CLOCK = 13
INTERRUPT = 15

gpio.setup([DATA, CLOCK], gpio.IN)
gpio.setup(INTERRUPT, gpio.OUT, initial=gpio.HIGH)
