import sys
import numpy as np
import cv2

from TrafficLight import findLight

video = cv2.VideoCapture('traffic.mp4')
success,image = video.read()
count = 0
while success:
    cv2.imwrite("test.jpg", image)
    if findLight() == True :
        print("RED")
    else :
        print("NONE")
    count = count + 1
    success, image = video.read()
video.release()
cv2.destroyAllWindows()
