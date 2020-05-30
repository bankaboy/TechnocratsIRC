#from Sensors.Sensor import Sensor1

sensorBytes = bytearray([i for i in range(20)])

def parseCommand(bytes):
    prefix = 0xf00
    firstCommand = 0x0f0
    secondCommand = 0x00f
    x = int.from_bytes(bytes, byteorder='little', signed=False)

	# check prefix for soil sensor selection
    if x&prefix== 0x800:
        print("Sensor Values")
        return sensorBytes

# print(parseBase('F').to_bytes(5, 'little'))
# parseCommand(0x320.to_bytes(3, 'little'))

"""
Reference:
https://github.com/technocratsroboticsvitc/rover/blob/master/BaseRoverComm/sockets/test/parseCommand.py
"""

import serial
import os

PORT = '/dev/xbee'
BUFFER_SIZE =  3

ser = serial.Serial(PORT)

try:
    while True:
        try:
            data = ser.read(BUFFER_SIZE)
            x=parseCommand(data)
            print("\n")
            # value = x.to_bytes(4,'little')
            ser.write(x)
        except Exception as e:
            print(e)
            ser.close()
            ser = serial.Serial(PORT)
except Exception as e:
    print(e)
finally:
    ser.close()
