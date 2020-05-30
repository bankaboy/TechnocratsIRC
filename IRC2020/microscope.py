import cv2 

def viewImage(image,name):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

camera = cv2.VideoCapture(2)

ret , frame = camera.read()
viewImage(frame,'soil_image')

camera.release()