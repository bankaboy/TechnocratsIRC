#from Sensors.Sensor import Sensor1
from Sensor import Sensor
import serial
import os

PORT = '/dev/xbee'
BUFFER_SIZE =  3

ser = serial.Serial(PORT)

sensorBytes = bytearray([i for i in range(20)])

def parseCommand(bytes):
    prefix = 0xf00
    firstCommand = 0x0f0
    secondCommand = 0x00f
    x = int.from_bytes(bytes, byteorder='little', signed=False)
    
    # check prefix for base motor
    if x&prefix == 0x000:
        print('Base Motor')

        if x&firstCommand==0x040:
            print('Forward')
            cmd="python demo.py 87"
            os.system(cmd)
            return
            # return 87
        elif x&firstCommand==0x050:
            print('Backward')
            cmd="python demo.py 83"
            os.system(cmd)
            return
            # return 83
        elif x&firstCommand==0x060:
            print('Left')
            cmd="python demo.py 65"
            os.system(cmd)
            return
            # return 65
        elif x&firstCommand==0x070:
            print('Right')
            cmd="python demo.py 68"
            os.system(cmd)
            return
            # return 68
        else:
            print('Stop')
            cmd="python demo.py 27"
            os.system(cmd)
            return
            # return 27

	# check prefix for camera
    elif x&prefix == 0x100:
	    print('Camera Control')
	    if x&firstCommand == 0x000:
		    print('Camera 1')
	    elif x&firstCommand == 0x010:
	    	print('Camera 2')
	    elif x&firstCommand == 0x020:
	    	print('Camera 3')
	    elif x&firstCommand == 0x030:
	    	print('Camera 4')
	    else:
	    	print("Invalid Camera")

	# check prefix for arm motor control
    elif x&prefix== 0x200:
        print("Base Arm Control")
        if x&firstCommand == 0x020:
            print("Motor Left")
            cmd="python demo.py 50"
            os.system(cmd)
            return
            # return 50
        elif x&firstCommand == 0x030:
            print("Motor Right")
            cmd="python demo.py 49"
            os.system(cmd)
            return
            # return 49
        else:
            print("Stop")
            cmd="python demo.py 32"
            os.system(cmd)
            return
            # return 32

	# check prefix for actuator 1 control
    elif x&prefix== 0x300:
        print("Actuator 1 Control")
        if x&firstCommand == 0x020:
            print("Extend")
            cmd="python demo.py 51"
            os.system(cmd)
            return
            # return 51
        elif x&firstCommand == 0x030:
            print("Retract")
            cmd="python demo.py 52"
            os.system(cmd)
            return
            # return 52
        else:
            print("Stop")
            cmd="python demo.py 33"
            os.system(cmd)
            return
            # return 33

	# check prefix for actuator 2 control
    elif x&prefix== 0x400:
        print("Actuator 2 Control")
        if x&firstCommand == 0x020:
            print("Extend")
            cmd="python demo.py 53"
            os.system(cmd)
            return
            # return 53
        elif x&firstCommand == 0x030:
            print("Retract")
            cmd="python demo.py 54"
            os.system(cmd)
            return
            # return 54
        else:
            print("Stop")
            cmd="python demo.py 34"
            os.system(cmd)
            return
            # return 34
	
	# check prefix for actuator 3 control
    elif x&prefix== 0x500:
        print("Actuator 3 Control")
        if x&firstCommand == 0x020:
            print("Extend")
            cmd="python demo.py 55"
            os.system(cmd)
            return
            # return 55
        elif x&firstCommand == 0x030:
            print("Retract")
            cmd="python demo.py 56"
            os.system(cmd)
            return
            # return 56
        else:
            print("Stop")
            cmd="python demo.py 35"
            os.system(cmd)
            return
            # return 35

	# check prefix for gripper rotation control
    elif x&prefix== 0x600:
        print("Gripper Rotate Control")
        if x&firstCommand == 0x020:
            print("Motor Left")
            cmd="python demo.py 75"
            os.system(cmd)
            return
            # return 75
        elif x&firstCommand == 0x030:
            print("Motor Right")
            cmd="python demo.py 73"
            os.system(cmd)
            return
            # return 73
        else:
            print("Stop")
            cmd="python demo.py 37"
            os.system(cmd)
            return
            # return 37
	
	# check prefix for gripper claw 
    elif x&prefix== 0x700:
        print("Gripper Claw Control")
        if x&firstCommand == 0x020:
            print("Gripper Claw Open")
            cmd="python demo.py 71"
            os.system(cmd)
            return
            # return 71
        elif x&firstCommand == 0x030:
            print("Gripper Claw Close")
            cmd="python demo.py 84"
            os.system(cmd)
            return
            # return 84
        else:
            print("Gripper Claw Stop")
            cmd="python demo.py 36"
            os.system(cmd)
            return
            # return 36

	# check prefix for soil sensor selection
    elif x&prefix== 0x800:
        print("Soil Sensor")
        # with Sensor as roverSensor:
            # values = roverSensor.getAllSensorValue()
            # ser.write(values)
        '''
        In case curent approach does not work
        '''
        roverSensor = Sensor()
        values = roverSensor.getSensorValueBytes()
        ser.write(values)
        roverSensor.close()
        return        

	# check prefix for getting GPS value
    elif x&prefix == 0xa00:
        print("Get GPS")
    elif x&prefix == 0xb00:
        print("Soil Setup")
        if x&firstCommand == 0x010:
            print("Auger up")
        elif x&firstCommand == 0x020:
            print("Auger down")
        elif x&firstCommand == 0x030:
            print("Soil Collect")
        else:
            print("No change for soil setup")

	# check prefix for autonomous 
    elif x&prefix == 0xc00:
        print("Autonomous Commands")
        if x&firstCommand == 0x000:
            print("Start")
        elif x&firstCommand == 0x010:
            print("Left")
        elif x&firstCommand == 0x020:
            print("Right")
        elif x&firstCommand == 0x020:
            print("Stop")
        else:
            print("No change for autonomous command")

	# check prefix for adding GPS lattitue 
    elif x&prefix == 0xd00:
        print("Add GPS Lat")

    # check prefix for adding GPS longitude
    elif x&prefix == 0xe00:
        print("Add GPS Long")

    # check prefix for RPM change 
    elif x&prefix == 0xf00:
        print("RPM Control")
        if x&firstCommand == 0x020:
            print("Increase RPM")
            cmd="python demo.py 43"
            os.system(cmd)
            return
            # return 43
        elif x&firstCommand == 0x030:
            print("Decrease RPM")
            cmd="python demo.py 45"
            os.system(cmd)
            return
            # return 45
        else:
            print("No change for RPM control")
    else:
        print("Invalid Prefix")


# print(parseBase('F').to_bytes(5, 'little'))
# parseCommand(0x320.to_bytes(3, 'little'))

"""
Reference:
https://github.com/technocratsroboticsvitc/rover/blob/master/BaseRoverComm/sockets/test/parseCommand.py
"""

try:
    while True:
        try:
            data = ser.read(BUFFER_SIZE)
            parseCommand(data)
            print("\n")
            # cmd="python demo.py " +str(x)
            # os.system(cmd)
        except Exception as e:
            print(e)
            ser.close()
            ser = serial.Serial(PORT)
except Exception as e:
    print(e)
finally:
    ser.close()
#from Sensors.Sensor import Sensor1
from Sensor import Sensor
import serial
import os

PORT = '/dev/xbee'
BUFFER_SIZE =  3

ser = serial.Serial(PORT)

sensorBytes = bytearray([i for i in range(20)])

def parseCommand(bytes):
    prefix = 0xf00
    firstCommand = 0x0f0
    secondCommand = 0x00f
    x = int.from_bytes(bytes, byteorder='little', signed=False)
    
    # check prefix for base motor
    if x&prefix == 0x000:
        print('Base Motor')

        if x&firstCommand==0x040:
            print('Forward')
            cmd="python demo.py 87"
            os.system(cmd)
            return
            # return 87
        elif x&firstCommand==0x050:
            print('Backward')
            cmd="python demo.py 83"
            os.system(cmd)
            return
            # return 83
        elif x&firstCommand==0x060:
            print('Left')
            cmd="python demo.py 65"
            os.system(cmd)
            return
            # return 65
        elif x&firstCommand==0x070:
            print('Right')
            cmd="python demo.py 68"
            os.system(cmd)
            return
            # return 68
        else:
            print('Stop')
            cmd="python demo.py 27"
            os.system(cmd)
            return
            # return 27

	# check prefix for camera
    elif x&prefix == 0x100:
	    print('Camera Control')
	    if x&firstCommand == 0x000:
		    print('Camera 1')
	    elif x&firstCommand == 0x010:
	    	print('Camera 2')
	    elif x&firstCommand == 0x020:
	    	print('Camera 3')
	    elif x&firstCommand == 0x030:
	    	print('Camera 4')
	    else:
	    	print("Invalid Camera")

	# check prefix for arm motor control
    elif x&prefix== 0x200:
        print("Base Arm Control")
        if x&firstCommand == 0x020:
            print("Motor Left")
            cmd="python demo.py 50"
            os.system(cmd)
            return
            # return 50
        elif x&firstCommand == 0x030:
            print("Motor Right")
            cmd="python demo.py 49"
            os.system(cmd)
            return
            # return 49
        else:
            print("Stop")
            cmd="python demo.py 32"
            os.system(cmd)
            return
            # return 32

	# check prefix for actuator 1 control
    elif x&prefix== 0x300:
        print("Actuator 1 Control")
        if x&firstCommand == 0x020:
            print("Extend")
            cmd="python demo.py 51"
            os.system(cmd)
            return
            # return 51
        elif x&firstCommand == 0x030:
            print("Retract")
            cmd="python demo.py 52"
            os.system(cmd)
            return
            # return 52
        else:
            print("Stop")
            cmd="python demo.py 33"
            os.system(cmd)
            return
            # return 33

	# check prefix for actuator 2 control
    elif x&prefix== 0x400:
        print("Actuator 2 Control")
        if x&firstCommand == 0x020:
            print("Extend")
            cmd="python demo.py 53"
            os.system(cmd)
            return
            # return 53
        elif x&firstCommand == 0x030:
            print("Retract")
            cmd="python demo.py 54"
            os.system(cmd)
            return
            # return 54
        else:
            print("Stop")
            cmd="python demo.py 34"
            os.system(cmd)
            return
            # return 34
	
	# check prefix for actuator 3 control
    elif x&prefix== 0x500:
        print("Actuator 3 Control")
        if x&firstCommand == 0x020:
            print("Extend")
            cmd="python demo.py 55"
            os.system(cmd)
            return
            # return 55
        elif x&firstCommand == 0x030:
            print("Retract")
            cmd="python demo.py 56"
            os.system(cmd)
            return
            # return 56
        else:
            print("Stop")
            cmd="python demo.py 35"
            os.system(cmd)
            return
            # return 35

	# check prefix for gripper rotation control
    elif x&prefix== 0x600:
        print("Gripper Rotate Control")
        if x&firstCommand == 0x020:
            print("Motor Left")
            cmd="python demo.py 75"
            os.system(cmd)
            return
            # return 75
        elif x&firstCommand == 0x030:
            print("Motor Right")
            cmd="python demo.py 73"
            os.system(cmd)
            return
            # return 73
        else:
            print("Stop")
            cmd="python demo.py 37"
            os.system(cmd)
            return
            # return 37
	
	# check prefix for gripper claw 
    elif x&prefix== 0x700:
        print("Gripper Claw Control")
        if x&firstCommand == 0x020:
            print("Gripper Claw Open")
            cmd="python demo.py 71"
            os.system(cmd)
            return
            # return 71
        elif x&firstCommand == 0x030:
            print("Gripper Claw Close")
            cmd="python demo.py 84"
            os.system(cmd)
            return
            # return 84
        else:
            print("Gripper Claw Stop")
            cmd="python demo.py 36"
            os.system(cmd)
            return
            # return 36

	# check prefix for soil sensor selection
    elif x&prefix== 0x800:
        print("Soil Sensor")
        with Sensor as roverSensor:
            values = roverSensor.getAllSensorValue()
            ser.write(values)
        '''
        In case curent approach does not work
        roverSensor = Sensor()
        values = roverSensor.getAllSensorValue()
        roverSensor.close()
        ser.write(values)
        '''
        return        

	# check prefix for getting GPS value
    elif x&prefix == 0xa00:
        print("Get GPS")
    elif x&prefix == 0xb00:
        print("Soil Setup")
        if x&firstCommand == 0x010:
            print("Auger up")
        elif x&firstCommand == 0x020:
            print("Auger down")
        elif x&firstCommand == 0x030:
            print("Soil Collect")
        else:
            print("No change for soil setup")

	# check prefix for autonomous 
    elif x&prefix == 0xc00:
        print("Autonomous Commands")
        if x&firstCommand == 0x000:
            print("Start")
        elif x&firstCommand == 0x010:
            print("Left")
        elif x&firstCommand == 0x020:
            print("Right")
        elif x&firstCommand == 0x020:
            print("Stop")
        else:
            print("No change for autonomous command")

	# check prefix for adding GPS lattitue 
    elif x&prefix == 0xd00:
        print("Add GPS Lat")

    # check prefix for adding GPS longitude
    elif x&prefix == 0xe00:
        print("Add GPS Long")

    # check prefix for RPM change 
    elif x&prefix == 0xf00:
        print("RPM Control")
        if x&firstCommand == 0x020:
            print("Increase RPM")
            cmd="python demo.py 43"
            os.system(cmd)
            return
            # return 43
        elif x&firstCommand == 0x030:
            print("Decrease RPM")
            cmd="python demo.py 45"
            os.system(cmd)
            return
            # return 45
        else:
            print("No change for RPM control")
    else:
        print("Invalid Prefix")


# print(parseBase('F').to_bytes(5, 'little'))
# parseCommand(0x320.to_bytes(3, 'little'))

"""
Reference:
https://github.com/technocratsroboticsvitc/rover/blob/master/BaseRoverComm/sockets/test/parseCommand.py
"""

try:
    while True:
        try:
            data = ser.read(BUFFER_SIZE)
            parseCommand(data)
            print("\n")
            # cmd="python demo.py " +str(x)
            # os.system(cmd)
        except Exception as e:
            print(e)
            ser.close()
            ser = serial.Serial(PORT)
except Exception as e:
    print(e)
finally:
    ser.close()
