import cv2
import  numpy as np
from myUtilities import stackImages
from myUtilities import kernel
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold 1", "Parameters", 23, 255, empty)
cv2.createTrackbar("Threshold 2", "Parameters", 20, 255, empty)
cv2.createTrackbar("Minimum Area", "Parameters", 5000, 30000, empty)

# assign threshold 1 and 2 to the values on the trackbars
threshold1 = cv2.getTrackbarPos("Threshold 1", "Parameters")
threshold2 = cv2.getTrackbarPos("Threshold 2", "Parameters")
areaMin = cv2.getTrackbarPos("Minimum Area", "Parameters")

def getContours(img, imgContour):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)#True indicates a closed contour
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5);
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),5)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),5)


while True:
    success, img = cap.read()
    imgContour = img.copy()
    imgBlur = cv2.GaussianBlur(img, (7,7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    imgDilated = cv2.dilate(imgCanny, kernel, iterations = 1)

    getContours(imgDilated, imgContour)

    imgStack = stackImages(0.8, ([img, imgCanny, imgContour]))

    cv2.imshow("Result", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
