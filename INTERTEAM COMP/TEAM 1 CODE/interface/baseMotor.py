from nanpy import ArduinoApi, SerialManager
import time

class Motor():
  # Works as setup()
  def __init__(self, device):
    self.devicePath = device
    self.connection = SerialManager(device=self.devicePath)
    self.arduino = ArduinoApi(connection=self.connection)
    self.RPM = 70
    self.turnPRM = 60

    # Motor pins

    self.d0 = 2
    self.pwm0 = 3

    self.d0 = 4
    self.pwm0 = 5

    self.d0 = 2
    self.pwm0 = 5

    self.d0 = 2
    self.pwm0 = 5

    self.d0 = 2
    self.pwm0 = 5

    self.d0 = 2
    self.pwm0 = 5

    # Setup pinmodes
    self.arduino.pinMode(self.dir11, self.arduino.OUTPUT)
    self.arduino.pinMode(self.pwm11, self.arduino.OUTPUT)
    self.arduino.pinMode(self.dir12, self.arduino.OUTPUT)
    self.arduino.pinMode(self.pwm12, self.arduino.OUTPUT)
    self.arduino.pinMode(self.dir21, self.arduino.OUTPUT)
    self.arduino.pinMode(self.pwm21, self.arduino.OUTPUT)
    self.arduino.pinMode(self.dir22, self.arduino.OUTPUT)
    self.arduino.pinMode(self.pwm22, self.arduino.OUTPUT)

  def moveMotor(self, direction):
    if direction=='f':
      self.forwardMotor()
    elif direction=='b':
      self.backwardMotor()
    elif direction=='l':
      self.leftMotor()
    elif direction=='r':
      self.rightMotor()
    elif direction=='s':
      self.resetAllMotors()
    elif direction=='x':
      exit()    
  
  def forwardMotor(self):
    self.arduino.digitalWrite(self.dir11, self.arduino.HIGH)
    self.arduino.digitalWrite(self.dir12, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir21, self.arduino.HIGH)
    self.arduino.digitalWrite(self.dir22, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir21, self.arduino.HIGH)
    self.arduino.digitalWrite(self.dir22, self.arduino.LOW)

    self.arduino.analogWrite(self.pwm11, self.RPM)
    self.arduino.analogWrite(self.pwm12, self.RPM)
    self.arduino.analogWrite(self.pwm21, self.RPM)
    self.arduino.analogWrite(self.pwm22, self.RPM)
    self.arduino.analogWrite(self.pwm21, self.RPM)
    self.arduino.analogWrite(self.pwm22, self.RPM)

  def backwardMotor(self):
    self.arduino.digitalWrite(self.dir11, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir12, self.arduino.HIGH)
    self.arduino.digitalWrite(self.dir21, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir22, self.arduino.HIGH)
    self.arduino.digitalWrite(self.dir21, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir22, self.arduino.LOW)

    self.arduino.analogWrite(self.pwm11, self.RPM)
    self.arduino.analogWrite(self.pwm12, self.RPM)
    self.arduino.analogWrite(self.pwm21, self.RPM)
    self.arduino.analogWrite(self.pwm22, self.RPM)
    self.arduino.analogWrite(self.pwm21, self.RPM)
    self.arduino.analogWrite(self.pwm22, self.RPM)

  def leftMotor(self):
    self.arduino.digitalWrite(self.dir11, self.arduino.HIGH)
    self.arduino.digitalWrite(self.dir12, self.arduino.HIGH)
    self.arduino.digitalWrite(self.dir21, self.arduino.HIGH)
    self.arduino.digitalWrite(self.dir22, self.arduino.HIGH)
    self.arduino.digitalWrite(self.dir21, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir22, self.arduino.LOW)

    self.arduino.analogWrite(self.pwm11, self.turnRPM)
    self.arduino.analogWrite(self.pwm12, self.turnRPM)
    self.arduino.analogWrite(self.pwm21, self.turnRPM)
    self.arduino.analogWrite(self.pwm22, self.turnRPM)
    self.arduino.analogWrite(self.pwm21, self.turnRPM)
    self.arduino.analogWrite(self.pwm22, self.turnRPM)

  def rightMotor(self):
    self.arduino.digitalWrite(self.dir11, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir12, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir21, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir22, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir21, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir22, self.arduino.LOW)

    self.arduino.analogWrite(self.pwm11, self.turnRPM)
    self.arduino.analogWrite(self.pwm12, self.turnRPM)
    self.arduino.analogWrite(self.pwm21, self.turnRPM)
    self.arduino.analogWrite(self.pwm22, self.turnRPM)
    self.arduino.analogWrite(self.pwm21, self.turnRPM)
    self.arduino.analogWrite(self.pwm22, self.turnRPM)

  def resetAllMotors(self):
    self.arduino.analogWrite(self.pwm11,0)
    self.arduino.analogWrite(self.pwm12,0)
    self.arduino.analogWrite(self.pwm21,0)
    self.arduino.analogWrite(self.pwm22,0)
    self.arduino.analogWrite(self.pwm21,0)
    self.arduino.analogWrite(self.pwm22,0)
