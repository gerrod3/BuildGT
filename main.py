import sys
import numpy as np
import cv2

from TrafficLight import findLight

video = cv2.VideoCapture('traffic.mp4')
success,image = video.read()
count = 0




while success:
    cv2.imwrite("test.jpg", image)
    result, modImg = findLight("red", False)
    if result :
        print("RED")
    else :
        print("NONE")
    count = count + 1
    cv2.imshow("video", modImg)
    if cv2.waitKey(33) == 27: 
		break
    success, image = video.read()

video.release()
cv2.destroyAllWindows()
