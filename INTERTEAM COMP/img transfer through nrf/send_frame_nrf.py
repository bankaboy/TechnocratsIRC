import numpy as np
import time
import cv2 as cv
import pickle #check with bytes transfer first, then with pickle, advantage - easy reconstruction
import serial as sl

ser = sl.Serial('/dev/ttyACM0',9600) #initialize to address of bot arduino

camera = cv.VideoCapture(0)
while True:
    ret,frame = camera.read() #don't remove ret, otherwise will also send TRUE/FALSE along with frame array
    print(type(frame))
    #print(frame)
    print(len(frame))    
    #convrt to bytes and send via rf to base
    #frame_string = pickle.dumps(frame)
    print(frame.shape)
    frame_nrf = frame.tobytes()
    ser.write(frame_nrf)
    #cv.imwrite('feed_atrover.jpg',frame)
    #time.sleep(1)
    break
    # break statement is to only test for one frame, for complete video remove it
