#from Sensors.Sensor import Sensor1

sensorBytes = bytearray([i for i in range(20)])

def parseCommand(bytes):
    prefix = 0xf00
    firstCommand = 0x0f0
    secondCommand = 0x00f
    x = int.from_bytes(bytes, byteorder='little', signed=False)

	# check prefix for soil sensor selection
    if x&prefix== 0x800:
        print("Soil Sensor")
        if x&firstCommand == 0x080:
            print("Sensor 1 : moisture")
            x = sensorBytes[0]
            return x
        elif x&firstCommand == 0x040:
            print("Sensor 2 : pH")
            x = sensorBytes[1]
            return x
        elif x&firstCommand == 0x020:
            print("Sensor 3 : uv")
            x = sensorBytes[2]
            return x
        elif x&firstCommand == 0x010:
            print("Sensor 4 : methane")
            x = sensorBytes[3]
            return x
        elif x&secondCommand == 0x08:
            print("Sensor 5 : temp")
            return int.from_bytes(sensorBytes[4:6],byteorder='little',signed=False)
        elif x&secondCommand == 0x04:
            print("Sensor 6: pressure")
            return int.from_bytes(sensorBytes[8:12],byteorder='little',signed=False)
        elif x&secondCommand == 0x02:
            print("Sensor 7 : atm_temp")
            return int.from_bytes(sensorBytes[12:16],byteorder='little',signed=False)
        elif x&secondCommand == 0x01:
            print("Sensor 8 : atm_humidity")
            return int.from_bytes(sensorBytes[16:20],byteorder='little',signed=False)
        else:
            print("No change for soil sensor command")
            return
	# check prefix for electrical sensor selection
    elif x&prefix== 0x900:
        print("Current/ Soil Sensor")
        if x&firstCommand == 0x080:
            print("Current Sensor 1")
        elif x&firstCommand == 0x040:
            print("Current Sensor 2")
        elif x&firstCommand == 0x020:
            print("Current Sensor 3")
        elif x&firstCommand == 0x010:
            print("Current Sensor 4")
        elif x&secondCommand == 0x08:
            print("Current Sensor 5")
        elif x&secondCommand == 0x04:
            print("Current Sensor 6")
        elif x&secondCommand == 0x02:
            print("Voltage Sensor 1")
            return sensorBytes[6]
        elif x&secondCommand == 0x01:
            print("Voltage Sensor 2")
            return sensorBytes[7]
        else:
            print("No change for electrical sensor command")

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
            value = x.to_bytes(4,'little')
            ser.write(value)
        except Exception as e:
            print(e)
            ser.close()
            ser = serial.Serial(PORT)
except Exception as e:
    print(e)
finally:
    ser.close()
