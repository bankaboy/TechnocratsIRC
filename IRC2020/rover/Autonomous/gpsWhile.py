import serial

port = "/dev/ttyS0"
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
try:
	while True:
		try:
    			data = ser.readline().decode().split(',')
    			if(data[0]=="$GNGGA"):
    				print(float(data[2])/100,float(data[4])/100)
		except Exception as e:
			print(str(e))
			ser.close()
			ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
finally:
	ser.close()

