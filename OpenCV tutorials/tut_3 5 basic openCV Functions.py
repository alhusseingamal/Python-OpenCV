import cv2
import numpy as np
path = "Resources/blanca.PNG"

kernel = np.ones((5, 5), np.uint8)
print(kernel )
# cvtColor, GaussianBlur, Canny
img = cv2.imread(path) # if we do cv2.imread(path, 0) the image is automatically converted into greyscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # this is the more standard way of converting
imgBlur = cv2.GaussianBlur(imgGray,(15, 15), 0) # first parameter is the image to be blurred
# (5,5) is the dimension of the kernel: increasing it increases blur, and it can only be in odd numbers
# 0 is called the sigma value
imgCanny = cv2.Canny(imgBlur, 10, 10)
# the 2nd and 3rd parameters are called the threshold parameters; the number of edges in detection; decreasing them, increases the number of edges detected
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
# increasing the number of iterations increases the thickness of the edge lines
imgErosion = cv2.erode(imgDilation, kernel, iterations = 1)
# erode does the reverse of dilate function, but most likely it won't be able to restore the original quality of the image before dilation
cv2.imshow("Blanca", img)
cv2.imshow("Blanca in GreyScale", imgGray)
cv2.imshow("Blanca in GreyScale and Blur", imgBlur)
cv2.imshow("Blanca in GreyScale, Blur and Canny", imgCanny)
cv2.imshow("Blanca in GreyScale, Blur, Canny, and Dilation", imgDilation)
cv2.imshow("Blanca in GreyScale, Blur, Canny, Dilation and Erosion", imgErosion)
cv2.waitKey(0)

