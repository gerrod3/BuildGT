import sys
import numpy as np
import cv2
import RPi.GPIO as GPIO

from TrafficLight import findLight
from carTest import findCar

video = cv2.VideoCapture('traffic.mp4')
success,image = video.read()
count = 0

show = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

while success:
    cv2.imwrite("test.jpg", image)
    result, modImage = findLight("red")
    result2, carImage = findCar()
    result = result and result2
    if result :
        print("RED")
        state = GPIO.input(18)
        if state == False:
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(15,GPIO.LOW)
    else :
        print("NONE")
        state = GPIO.input(15)
        if state == False:
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.LOW)
    count = count + 1

    success, image = video.read()
    if show:
        cv2.imshow("Filtered", modImage)
        if cv2.waitKey(33) == 27:
            break

GPIO.output(15,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
video.release()
cv2.destroyAllWindows()
