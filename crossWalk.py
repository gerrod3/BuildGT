import numpy as np
import cv2

cap = cv2.VideoCapture('traffic.mp4') 
success, img = cap.read()
#crop_img = img[img.shape[0]/2:img.shape[0]]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

low_threshold = 100
high_threshold = 300
edges = cv2.Canny(gray, low_threshold, high_threshold)

rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 15  # minimum number of votes (intersections in Hough grid cell)
min_line_length = 50  # minimum number of pixels making up a line
max_line_gap = 20  # maximum gap in pixels between connectable line segments
line_image = np.copy(img) * 0  # creating a blank to draw lines on

# Run Hough on edge detected image
# Output "lines" is an array containing endpoints of detected line segments
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                    min_line_length, max_line_gap)

bound = 100

for line in lines:
    for x1,y1,x2,y2 in line:
        
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

    # Draw the lines on the  image
lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)

cv2.imshow("Lines", lines_edges)
cv2.waitKey(0)