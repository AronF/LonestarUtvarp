import RPi.GPIO as gpio
from .pindefs import *

def isAM():
    return not gpio.input(FMAM)
