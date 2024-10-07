import pyfirmata
import time

port = 'COM3'

board = pyfirmata.Arduino(port) # To open the port COM linked to the Arduino card

your_component_pin = board.get_pin('a:0:i') # To initialize the pin used

iterator = pyfirmata.util.Iterator(board) # to initialize the link between the card and python

iterator.start() # To start the connection

your_component_pin.enable_reporting() # to read the values

while your_component_pin.read() == None: #None  As long as there is no value
    try:
        while True:
            print ('The value is  : ',your_component_pin.read()) # Read and display the values
            time.sleep(1) # Delay between two measures
    except:
       your_component_pin.disable_reporting()
       board.exit()

# Here is the modification you have to do make a program for your component:

# Which is highlight in turquoise can be replaced by the name of your component such as push button or motor. Don’t forget to write what is after the dot. For example push_button.read() instead of your_component_pin.read().
# Which is highlight in Green  can be replaced by a value from the table:
 
# Input (sensor, button …)
# Output (motor, led …)
# d => digital (d : N° pin : i) (d : N° pin : o)
# a => analog (a : N° pin : i) (a : N° pin : o)
# Be careful, There are 2 exceptions for digital:
# 1) (d : N° pin: p) -> p means pulse width modulation  (pwm),  which permits you to vary the brightness of a led for example.
# 2) ( d : N° pin: s) -> s means servomotor.You have to use it only if your component is a servomotor.
# d = digital, we use it if we want to control a component (a motor for example)
# a = analog, we use it for all sensors which return a tension
# i = input
# o = output