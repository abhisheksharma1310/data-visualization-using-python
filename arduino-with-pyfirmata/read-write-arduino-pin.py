import pyfirmata
import time

board = pyfirmata.Arduino('COM15')

# keep reading all arduino pins value
it = pyfirmata.util.Iterator(board)
it.start()

# assign pin 10 as input pin
board.digital[10].mode = pyfirmata.INPUT

while True:
    #read value on pin 10
    sw = board.digital[10].read()
    #check for pin value
    if sw is True:
        # turn on led
        board.digital[13].write(1)
    else:
        # turn off led
        board.digital[13].write(0)
    time.sleep(1)


# assign pin 10 as input pin
switch = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

while True:
    #read value on pin 10
    sw = switch.read()
    #check for pin value
    if sw is True:
        # turn on led
        led.write(1)
    else:
        # turn off led
        led.write(0)
    time.sleep(1)


