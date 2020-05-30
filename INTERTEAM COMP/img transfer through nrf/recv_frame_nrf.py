import numpy as np
import cv2 as cv
import time
import pickle
import serial

#Define codec and create video writer object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('test_feed_atbase.avi',fourcc,24,(848,480))

ser = serial.Serial('/dev/ttyACM1',9600)
  
# receive data from the server
start = time.time()
while True:
    try:
        #section to repair frame
        #frame_arr = pickle.loads(frame)
        #print('Received',repr(frame_arr))
        #cv.imwrite('feed.jpg',newImg)
        frame = ser.read(480*640*3)
        frame_nrf = np.frombuffer(frame, dtype = np.uint8)
        print(frame_nrf)
        print(frame_nrf.shape)
        #print(data)
        frame_fin = frame_nrf.reshape((480,640,3))
        print(frame_fin)
        out.write(frame_arr)
        #print(count)
        break
        #break
    #except pickle.UnpicklingError:
    #    continue
    

