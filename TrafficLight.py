import numpy as np
import cv2
from PIL import Image
from os import path

def findLight() :
    image = cv2.imread("test.jpg")
    img_hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([170,0,0])
    upper_red = np.array([255,120,60])
    mask = cv2.inRange(img_hsv, lower_red, upper_red)
    rate = np.count_nonzero(mask) / 100000
    if rate > 0.10:
        return True
    else :
        return False
