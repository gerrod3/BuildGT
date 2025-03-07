# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import numpy
import cv2


def findCar() :
	image = cv2.imread("test.jpg")
	car_cascade = cv2.CascadeClassifier('cars.xml')
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cars = car_cascade.detectMultiScale(gray,3, 1,0, (10,10))
	for (x,y,w,h) in cars:
		cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

	if len(cars) == 0:
		return False, image
	else:
		return True, image

if __name__ == "__main__":
    video = cv2.VideoCapture('car.mp4')
    success,image = video.read()
    while success:
        cv2.imwrite("test.jpg", image)
        result, modImage = findCar()
        cv2.imshow("Filtered", modImage)
        if cv2.waitKey(33) == 27:
            break
        success, image = video.read()

video.release()
cv2.destroyAllWindows()
