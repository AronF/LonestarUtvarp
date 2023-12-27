import RPi.GPIO as gpio
from .pindefs import *

def isFM():
    return not gpio.input(FMAM)
