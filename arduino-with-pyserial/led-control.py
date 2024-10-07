import serial
import time

arduinoData = serial.Serial('COM15', 9600)

def led_on():
    arduinoData.write(b'1') #b'1'

def led_off():
    arduinoData.write(b'0') #b'0'

while True:
    led_on()
    print("Led On")
    time.sleep(1)
    led_off()
    print("Led off")
    time.sleep(1)

