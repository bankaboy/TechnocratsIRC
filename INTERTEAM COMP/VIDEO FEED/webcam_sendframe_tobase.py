import numpy as np
import socket
import time
import cv2 as cv
import pickle

PORT = 8002

s = socket.socket()
s.bind(('',PORT))
s.listen(5)

c,addr = s.accept()

count = 0

camera = cv.VideoCapture(0)
while True:
    ret,frame = camera.read()
    #count= count+1
    #don't remove ret, otherwise socket will also send TRUE/FALSE along with frame array
    #print(type(frame))
    print(frame)
    #print(len(frame))
    #c.send(str(frame).encode('ascii'))
    #convrt to bytes and send via socket to base
    frame_string = pickle.dumps(frame)
    c.send(frame_string)
    #frame_base = frame.tobytes()
    print(frame.shape)
    #c.send(frame_base)
    cv.imwrite('feed_atrover.jpg',frame)
    #time.sleep(1)
    #break
    #if count == 10:
    #    break
    #time.sleep(2)
    #statement is to only test for one frame, for complete video remove it
