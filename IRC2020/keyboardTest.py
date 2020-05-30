import serial
import time
import getch


ser = serial.Serial('/dev/ttyACM1',baudrate = 9600 ,timeout = 0.001)

def getValue1():
    ser.write(b'a')
def getValue2():
    ser.write(b'd')

while 1:
    userInput = getch.getch()

    if userInput == 'a':
        getValue1()
    elif userInput == 'd':
        getValue2()



