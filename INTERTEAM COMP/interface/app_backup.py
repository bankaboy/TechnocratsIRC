from flask import Flask, render_template, jsonify, request
import os
import re
import serial
from baseMotor import Motor

app = Flask(__name__)

# ================
# Global Variables
# ================
motorPath = "/dev/ttyACM0"
motorConnected=False

# ================
# Connecting Motor
# ================
'''
try:
	roverMotor = Motor(motorPath)
	motorConnected=True
except serial.serialutil.SerialException:
	motorConnected = False
'''

@app.route("/")
def renderHome():
	dir = os.listdir("/dev/")
	regex = re.compile("^tty.*$")
	dir = list(filter(regex.match, dir))
	print(dir)
	return render_template("index.html", options=dir)


@app.route("/setMotors", methods=['GET'])
def getSetMotors():
	global baseMotor
	try:
		if request.args.get('reset'):
			# resetMotor(roverMotor)
			return "Reset!"
		if request.args['front']=='true':
			# roverMotor.moveMotor('forward')
			return "Forward"
		elif request.args['right']=='true':
			# roverMotor.moveMotor('right')
			return "Right"
		elif request.args['back']=='true':
			# roverMotor.moveMotor('backward')
			return "Backward"
		elif request.args['left']=='true':
			# roverMotor.moveMotor('left')
			return "Left"
		elif request.args['stop']=='true':
			# roverMotor.moveMotor('stop')
			return "Stopped!"
		# elif request.args['gearup']=='true':
		# 	return "Motor Speed: "+str(roverMotor.incrementRPM())
		# elif request.args['geardown']=='true':
		# 	return "Motor Speed: "+str(roverMotor.decrementRPM())
		else:
			return "Error: Unknown Command!"
	except KeyError:
		return "Error: Unknown Key!"

@app.route("/setRPM/<value>")
def setRPM(value):
	return value

app.run(debug=True, port=3000)
