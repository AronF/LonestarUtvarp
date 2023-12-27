import RPi.GPIO as gpio
from .pindefs import *

def isAM():
    return gpio.input(FMAM)
