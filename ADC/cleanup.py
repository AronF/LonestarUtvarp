import RPi.GPIO as gpio

#call this once execution is finished
def cleanup():
    gpio.cleanup()
