import RPi.GPIO as gpio

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
    return decode(data)

def decode(bytes):
    upper = bytes >> 8
    lower = bytes & 0x00FF
    return (upper, lower)
