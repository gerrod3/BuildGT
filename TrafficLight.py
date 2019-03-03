import numpy as np
import cv2
from PIL import Image
from os import path

lower_red = np.array([70, 70, 70], dtype = "uint8")
upper_red = np.array([255, 255, 255], dtype = "uint8")

lower_white = np.array([240, 240, 240])
upper_white = np.array([255, 255, 255])

colors = {"red" : (lower_red, upper_red), "white" : (lower_white, upper_white)}


def findLight(clr , modify = False) :
    image = cv2.imread("test.jpg")
    img_hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(img_hsv, colors[clr][0], colors[clr][1])
    rate = np.count_nonzero(mask) / 100000.0

    if modify:
        maskImage = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)
       # maskImage = cv2.bitwise_and(image, image, mask = mask)
        #image = np.hstack([img_hsv, maskImage])
        image = maskImage

    if rate > 0.004:
        return True, image
    else :
        return False, image
