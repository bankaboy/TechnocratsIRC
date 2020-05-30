import time
import cv2
import numpy as np

cap=cv2.VideoCapture('test_feed_atbase.avi')

while True:
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    time.sleep(.04)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
