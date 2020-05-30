#==============
#LIBRARIES
#==============

from gps import *
import time
import threading
from check_conn_ver2 import check_conn
import collections

#=================
#GLOBAL VARIABLES
#=================

MAX_LOCS = 10
locs = collections.deque([])  # queue of locations
currentLoc = None # current location of bot 
nextLoc = None # next location in list
prevLoc = None # previous location in list
localhost = "192.168.43.15"  #dhrubanka's mobile hotspot for now, change later

#============
# GPS_CLASS
#============

gpsd = None
class GpsPoller(threading.Thread):
   def __init__(self):
       threading.Thread.__init__(self)
       global gpsd
       gpsd=gps(mode=WATCH_ENABLE)
       self.current_value = None
       self.running = True
   def run(self):
       global gpsd
       while gpsp.running:
           gpsd.next()

#==========          
# MAIN 
#==========

gpsp = GpsPoller()

try:
   gpsp.start()

   while True:
      print("Still connected to localhost\n")
      print("Latitude: "+ str(gpsd.fix.latitude) + " , " + "Longitude: " + str(gpsd.fix.longitude) + "\n")
      time.sleep(1)
      lat, lon = gpsd.fix.latitude, gpsd.fix.longitude
      prevLoc = currentLoc
      currentLoc = (lat,lon)

      if check_conn(localhost):
         if len(locs) > MAX_LOCS:   # check if locs queue is full
            locs.pop()              # if it is full,(pop - remove form end)
            print("Earliest Location Removed\n")   # remove earliest location in locs queue
         locs.appendleft(currentLoc)  # add current, (appendleft - add to start) 
         print("Current Location Added\n")
         print("Current Location: "+str(curentLoc))
         print("Previous Location: "+str(curentLoc)+"\n")
      else:
         currentLoc = prevLoc
         print("No connection to localhost....Returning to previous location\n")
         print("Current Location: "+str(curentLoc))
         print("Previous Location: "+str(curentLoc)+"\n")
      
except(KeyboardInterrupt,SystemExit):
   gpsp.running = False
   gpsp.join()
