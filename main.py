import sys
import numpy as np
import cv2

from TrafficLight import findLight
#from Led import start
#from Led import stop

video = cv2.VideoCapture('traffic.mp4')
success,image = video.read()
count = 0


show = False

while success:
    #start()
    cv2.imwrite("test.jpg", image)
    result, modImage = findLight("red")
    if result :
        print("RED")
        #stop()
    else :
        print("NONE")
        #start()
    count = count + 1

    success, image = video.read()
    if show:
        cv2.imshow("Filtered", modImage)
        if cv2.waitKey(33) == 27:
            break

video.release()
cv2.destroyAllWindows()
