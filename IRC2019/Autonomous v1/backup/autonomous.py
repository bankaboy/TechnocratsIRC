#from matplotlib import pyplot as plt
import numpy as np
import math
import os
from compass import Compass
#from motor import Motor
#from roverGps import RoverGps
from time import sleep
from math import pi as PI

scale=10000
scaledLocations=[]
nextLocationIndex=0
roverMotor=None
# 12.842683 80.156161
# 12.842893, 80.156136
locations = [
	[12.842421, 80.155765],
	[12.842596, 80.155796],
	[12.842530, 80.155656],
	[12.842618, 80.155524],
	[12.842358, 80.155866]
]

# locations=np.array([
#   [80,20],
#   [90, 30],
#   [100, 40],
#   [110, 50]
# ])
def readGPS():
	f = open("/dev/serial0", mode='r')
	q = f.read().split('\n')
	sleep(3)
	for i in q:
		if i.split(',')[0]=='$GPGGA':
			a = float(i.split(',')[2].rstrip().lstrip())/100
			b = float(i.split(',')[4].rstrip().lstrip())/100
			print (a,b)
			return [a,b]
                                




def setScaledLocations():
	global scaledLocations
	global nextLocationIndex
	global locations
	locationOrigin = np.array(locations[0])
	locationsTranslated = [np.array([x, y])-locationOrigin for (x, y) in locations]

	scaledLocations=[[x*scale, y*scale] for (x, y) in locationsTranslated]
	# for i in scaledLocations:
	# print(scaledLocations)
#plt.scatter([x*scale for (x,y) in scaledLocation], [y*scale for (x, y) in scaledLocation])


def getSlope(currentLocation):
	global nextLocationIndex
	global scaledLocations
	global locations
	y1 = currentLocation[0]
	x1 = currentLocation[1]
	# print(scaledLocations)
	# 12.843469, 80.156470
	y2 = (locations[nextLocationIndex][0]-y1)*1000
	x2 = (locations[nextLocationIndex][1]-x1)*1000
	print(locations[nextLocationIndex], end=" ")

	try:
		slope = 90-math.atan(y2/x2)*180/PI
	except ZeroDivisionError:
		print("\n\nDivide by 0")
		return
	if(x2<0):
		slope=slope-180
	return slope

# TODO: Finish this function
def centerBot(compass, getAngle, roverGps, threshold=0):
	#currentLocation = roverGps.getGpsData()
	currentLocation = readGPS()
	#sleep(10)
	print(currentLocation)
	getAngle = getSlope(currentLocation)
	try:
		angle = compass.getCompassAngle()
	except ValueError:
		print("ValueError")
		return False
	try:
		if abs(abs(angle)-abs(getAngle))>threshold or np.sign(angle)!=np.sign(getAngle):
			if(angle<getAngle):
				print("Rotate right ", getAngle, angle)
				# roverMotor.rightMotor()
			else:
				print("Rotate Left ", getAngle, angle)
				# roverMotor.leftMotor()
			return False
		else:
			return True
	except TypeError:
		return False
	
# Steps:
# 1. Center the bot at north
# 2. Get the next Location slope
# 3. Rotate the bot that much angle
# 4. While the bot has not reached the location, move forward
# 5. If the bot is out of the slope angle, recenter it


def main():
	roverGps="dummy"
	global nextLocationIndex
	global locations
	botCentered = False
	locationAccuracy=0.00001
	# locationAccuracy=2
	initializedCurrentLocation=False

	print("Setting devices...")
	compass = Compass("/dev/ttyACM0")
	# roverMotor = Motor("/dev/ttyACM0")
#	roverGps = RoverGps()
	# roverMotor.resetAllMotors()
	print("All device set!")
	#sleep(10)

	# Set the bot to point at north
	while not botCentered:
		
		print("Centering Rover!",end=": ")
		if centerBot(compass, 0, roverGps, 10):
			botCentered=True
		# sleep(0.1)
		# os.system("clear")
	# botCentered=False
	
	os.system("clear")
	print("Rover centered!")
	# roverMotor.resetAllMotors()
	sleep(2)
	
	setScaledLocations()
	print(locations)
	sleep(2)
	
	while nextLocationIndex < len(locations):
	# while True:
		# roverMotor.resetAllMotors()
		try:
			currentLocation = readGPS()
#			currentLocation = roverGps.getGpsData()
			# print(roverGps)
			print(readGPS())
#			print(roverGps.getGpsData())
		except ValueError:
			print("GPS not set")
			continue
		if currentLocation[0]==None:
			print("GPs no locayion")
			continue
			
		if abs(currentLocation[0]-locations[nextLocationIndex][0])<locationAccuracy and  abs(currentLocation[1]-locations[nextLocationIndex][1])<locationAccuracy:
			nextLocationIndex+=1
			if nextLocationIndex>=len(locations):
				break
			print(locations)
			print("Location Reached!", currentLocation)
			print("Press any key to continue")
			input()
			# sleep(2)
			# Center bot to north
			botCentered=False
			while not botCentered:
				# os.system("clear")
				print("Centering Rover!",end=": ")
				if centerBot(compass, 0, roverGps, 20):
					print()
					botCentered=True
			botCentered=False
			print("Press anything to continue to location", locations[nextLocationIndex])
			input()
			continue
		
		slope = getSlope(currentLocation)
		# Move the rover to this slope    
		while not botCentered:
			# os.system("clear")
			slope = getSlope(currentLocation)
			try:
				print("Centering Rover ", end=': ')
			except ValueError:
				print("Value Error")
			if centerBot(compass, slope, roverGps, 15):
				botCentered=True
			# sleep(0.5)
		if not centerBot(compass, slope, roverGps, 15):
			print()
			botCentered=False

		# Move bot forward
		# os.system("clear")
		try:
			print("Move Forward", readGPS(), slope, compass.getCompassAngle(), abs(slope)-abs(compass.getCompassAngle()))
			#roverMotor.forwardMotor()
		except ValueError:
			print("Compass Value error")
	print("Finished!")
				


		

if __name__=="__main__":
	main()

