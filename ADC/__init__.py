import RPi.GPIO as gpio
from .getdata import getData
from .cleanup import cleanup

gpio.setmode(gpio.BOARD)

DATA = 11
CLOCK = 13
INTERRUPT = 15

gpio.setup([DATA, CLOCK], gpio.IN)
gpio.setup(INTERRUPT, gpio.OUT, initial=gpio.HIGH)
