import sys
import numpy as np
import cv2

from TrafficLight import findLight
from carTest import findCar

video = cv2.VideoCapture('traffic.mp4')
success,image = video.read()
count = 0

show = False

while success:
    cv2.imwrite("test.jpg", image)
    result, modImage = findLight("red")
    result2, carImage = findCar()
    result = result and result2
    if result :
        print("Stop")
    else :
        print("Go")
    count = count + 1
    cv2.imshow("Normal", cv2.imread("test.jpg"))
    cv2.imshow("TrafficData", modImage)
    cv2.imshow("CarData", carImage)
    success, image = video.read()
    if cv2.waitKey(33) == 27:
        break

video.release()
cv2.destroyAllWindows()
