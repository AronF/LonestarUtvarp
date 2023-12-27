import RPi.GPIO as gpio
from .pindefs import *

def ledOn():
    gpio.output(LED, 1)

def ledOff():
    gpio.output(LED, 0)
