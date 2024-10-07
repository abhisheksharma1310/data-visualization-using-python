import pyfirmata
port = 'COM3'# Windows
#port = '/dev/ttyACM3' # Linux
#port = '/dev/tty.usbmodem11401'# Mac
board = pyfirmata.Arduino(port) 
servo_pin = board.get_pin('d:9:s') # To initialize the pin used 

try :
    while True: # Infinite loop
        angle = int(input("Enter an angle between 10 and 170:)"))
        if angle < 10 : # If the value is lower than 10 degrees then we block the position  at 10 degrees of the servomotor
            angle = 10
        elif angle > 170 : # If the value is higher thant 170 degrees than we block the position at 170 degrees of the servomotor 
            angle = 170
            servo_pin.write(angle) # We assign this value into the servomotor 
except :
    board.exit()

