from nanpy import ArduinoApi, SerialManager
import time


class Motor():
  # Works as setup()
  def __init__(self, device):
    self.devicePath = device
    self.connection = SerialManager(device=self.devicePath)
    self.arduino = ArduinoApi(connection=self.connection)
    self.RPM1 = 100
    self.RPM2 = 100
    self.RPM3 = 100

    # Motor pins
    self.dir1=7
    self.pwm1=6

    self.dir2=12
    self.pwm2=9

    self.dir3=13
    self.pwm3=11

    # Setup pinmodes
    self.arduino.pinMode(self.dir1, self.arduino.OUTPUT)
    self.arduino.pinMode(self.pwm1, self.arduino.OUTPUT)
    self.arduino.pinMode(self.dir2, self.arduino.OUTPUT)
    self.arduino.pinMode(self.pwm2, self.arduino.OUTPUT)
    self.arduino.pinMode(self.dir3, self.arduino.OUTPUT)
    self.arduino.pinMode(self.pwm3, self.arduino.OUTPUT)
    
  def moveMotor(self, direction):
    if direction=='u':
      self.upMotor()
    elif direction=='d':
      self.downMotor()
    elif direction=='o':
      self.openMotor()
    elif direction=='c':
      self.closeMotor()
   # elif direction=='x':
    #  exit()
  def upMotor(self):
    self.arduino.digitalWrite(self.dir1, self.arduino.HIGH)
    self.arduino.digitalWrite(self.dir2, self.arduino.HIGH)
    
    self.arduino.analogWrite(self.pwm1, self.RPM1)
    self.arduino.analogWrite(self.pwm2, self.RPM1)
    time.sleep(1)
    self.arduino.analogWrite(self.pwm1, 0)
    self.arduino.analogWrite(self.pwm2, 0)

  def downMotor(self):
    self.arduino.digitalWrite(self.dir1, self.arduino.LOW)
    self.arduino.digitalWrite(self.dir2, self.arduino.LOW)
    self.arduino.analogWrite(self.pwm1, self.RPM1)
    self.arduino.analogWrite(self.pwm2, self.RPM2)
    time.sleep(1)
    self.arduino.analogWrite(self.pwm1, 0)
    self.arduino.analogWrite(self.pwm2, 0)


  def openMotor(self):
    self.arduino.digitalWrite(self.dir3, self.arduino.HIGH)
    self.arduino.analogWrite(self.pwm3, self.RPM3)
    time.sleep(1)
    self.arduino.analogWrite(self.pwm3, 0)

  def closeMotor(self):
    self.arduino.digitalWrite(self.dir3, self.arduino.LOW)
    self.arduino.analogWrite(self.pwm3, self.RPM3)
    time.sleep(1)
    self.arduino.analogWrite(self.pwm3, 0)
     

 
  
motor = Motor("COM16")
while True:
  direction=input('Enter:')
  motor.moveMotor(direction)



 
