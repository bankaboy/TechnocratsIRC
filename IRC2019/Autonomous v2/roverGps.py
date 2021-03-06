import gps
import serial
import threading


class RoverGps():
  def __init__(self):
    # self.devicePath = device
    #! Uncomment when running with gps module
    self.connectGPS()
    self.lat=None
    self.lon=None
    self.threadStart()
    #! debug only
    # self.lat=80
    # self.lon=20
    # self.count=0
    #! debug end
  
  def threadGpsValues(self):
    while True:
      report=self.session.next()
      if hasattr(report, 'lon'):
        # self.lon=round(float(report['lon'])*10000000)/10000000
        self.lon=round(float(report['lon']),6)
      if hasattr(report, 'lat'):
        self.lat=round(float(report['lat']),6)


  def threadStart(self):
    self.gpsThread = threading.Thread(target=self.threadGpsValues)
    self.gpsThread.start()
      
  def connectGPS(self):
    try:
      # GPS Socket
      self.session = gps.gps("localhost", "2947")
      self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    except Exception as e:
      raise e
  
  def getGpsData(self):
    # print(self.lat,self.lon)
    # Degub Only
    # self.count+=1
    # if self.count==100:
    #   self.count=0
    #   self.x+=1
    #   self.y+=1
    # return [self.x, self.y]
    # Debug end
    # print(self.session)
    # print(self.session.next())
    return [self.lat, self.lon]
    



# rover = RoverGps()
