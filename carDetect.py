# OpenCV Python program to detect cars in video frame 
# import libraries of python OpenCV 
import numpy
import cv2 

# capture frames from a video 
cap = cv2.VideoCapture('traffic.mp4') 

# Trained XML classifiers describes some features of some object we want to detect 
car_cascade = cv2.CascadeClassifier('cars.xml') 

def carInfront():
    image = cv2.imread("test.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 3, 1, 0, (100, 100))

    if len(cars) == 0: 
        return False
    else
        return True


