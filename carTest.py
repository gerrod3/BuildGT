# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import numpy
import cv2


def findCar() :
	image = cv2.imread("test.jpg")
	car_cascade = cv2.CascadeClassifier('cars.xml')
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cars = car_cascade.detectMultiScale(gray, 3, 1, 0, (100, 100))
	for (x,y,w,h) in cars:
		cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

	if len(cars) == 0:
		return False, image
	else:
		return True, image

cv2.destroyAllWindows()


