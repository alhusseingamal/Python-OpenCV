import cv2
import numpy as np
from myUtilities import stackImages

# Stacking images together can be done conventionally using matplotlib. It is fine with images, but the problem is it is too slow
# with videos and webcam

# numpy hstack combines numpy matrices horizontally, vstack combines numpy matrices vertically

# IMAGES
# path = "Resources/blanca.PNG"
# kernel = np.ones((5, 5), np.uint8)
# img = cv2.imread(path)
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(15, 15), 0)
# imgCanny = cv2.Canny(imgBlur, 10, 10)
# imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
# imgErosion = cv2.erode(imgDilation, kernel, iterations = 1)
# imgBlank = np.zeros((200,200), np.uint8)
# stackedImages = stackImages(0.2, ([img, imgGray, imgBlur],[imgCanny,imgDilation, imgErosion]))
# cv2.imshow("StackedImages", stackedImages)
# cv2.waitKey(0)

# WEBCAM

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
while True:
    success, img = cap.read()
    cv2.imshow("My camera", img)

    kernel = np.ones((5, 5), np.uint8)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(15, 15), 0)
    imgCanny = cv2.Canny(imgBlur, 10, 10)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
    imgErosion = cv2.erode(imgDilation, kernel, iterations = 1)
    imgBlank = np.zeros((200,200), np.uint8)
    
    stackedImages = stackImages(0.2, ([img, imgGray, imgBlur],[imgCanny,imgDilation, imgErosion]))
    cv2.imshow("StackedImages", stackedImages)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

