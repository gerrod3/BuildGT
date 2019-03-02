import sys
import numpy as np
import cv2

from TrafficLight import detect_traffic_lights

video = cv2.VideoCapture('traffic.mp4')
success,image = video.read()
count = 0
while success:
    if count % 50 == 0 :
        cv2.imwrite("./test/img_%d.jpg" % (count / 50), image)
    success, image = video.read()
    count = count + 1
print(count)
print(detect_traffic_lights("./test", 'faster_rcnn_resnet101_coco_11_06_2017', count, plot_flag=False))
video.release()
cv2.destroyAllWindows()
