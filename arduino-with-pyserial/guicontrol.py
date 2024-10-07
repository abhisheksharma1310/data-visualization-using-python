import serial
import tkinter

arduinoData = serial.Serial('COM15', 9600)

def led_on():
    arduinoData.write(b'1')

def led_off():
    arduinoData.write(b'0')

led_control_window = tkinter.Tk()
Button = tkinter.Button
btnOn = Button(led_control_window, text="Led ON", command=led_on)
btnOff = Button(led_control_window, text="Led OFF", command=led_off)
btnOn.grid(row=0, column=1)
btnOff.grid(row=1,column=1)
led_control_window.mainloop()