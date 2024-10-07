import pyfirmata
import time

port = 'COM3'# Windows
#port = '/dev/ttyACM3' # Linux
#port = '/dev/tty.usbmodem11401'# Mac

board = pyfirmata.Arduino(port) # To open the port COM linked to the Arduino card 

temperature_pin = board.get_pin('a:0:i') # To initialize the pin used 
iterator = pyfirmata.util.Iterator(board) # To initialized the link between Python and Arduino
iterator.start() # To start the connection
temperature_pin.enable_reporting() # Read the values from the pin 

while temperature_pin.read() == None: None # As long as there are no values

try:
    while True: # Infinite loop
        print ("temperature between 0 and 1 :",temperature_pin.read()) # We display the values read by the pin
        Celsius = ((temperature_pin.read()*5 - 0.5) *100)  # We transform the values in Celsius
        print ("temperature in Celsius :" ,(round(Celsius,4))) # We round and display the temperature
        time.sleep(1)# Delay of 1 second between two measures Fait une pause de 1 seconde entre deux mesures
except:
    temperature_pin.disable_reporting() #Stop reading value 
    board.exit( )


