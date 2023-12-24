import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

DATA = 11
CLOCK = 13
INTERRUPT = 15

gpio.setup([DATA,CLOCK], gpio.IN)
gpio.setup(INTERRUPT, gpio.OUT, initial = gpio.HIGH)


def getData():
    gpio.output(INTERRUPT, 0)
    data = 0
    for i in range(16):
        #busy wait for the clock to go high
        while not gpio.input(CLOCK): pass
        data <<= 1
        data |= gpio.input(DATA)
        #busy wait for the clock to go low again
        while gpio.input(CLOCK): pass
    gpio.output(INTERRUPT, 1)
    return data

def decode(bytes):
    upper = bytes >> 8
    lower = bytes & 0x00FF
    return (upper,lower)

def cleanup():
    gpio.cleanup()
