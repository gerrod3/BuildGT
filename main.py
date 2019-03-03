import sys
import numpy as np
import cv2
import RPi.GPIO as GPIO

from TrafficLight import findLight
from carTest import findCar

video = cv2.VideoCapture(0)
success,image = video.read()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

while success:
    cv2.imwrite("test.jpg", image)
    result1, modImage = findLight("red")
    result2, carImage = findCar()
    result = result1 and result2
    string = ""
    if result1:
        string.append("Red Light ")
    if result2:
        string.append("Car")
    if result :
        print("STOP, %s" % string)
        state = GPIO.input(18)
        if state == False:
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(12,GPIO.LOW)
    else :
        print("NONE")
        state = GPIO.input(12)
        if state == False:
            GPIO.output(12,GPIO.HIGH)
            GPIO.output(18,GPIO.LOW)
    success, image = video.read()

GPIO.output(12,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
video.release()
cv2.destroyAllWindows()
