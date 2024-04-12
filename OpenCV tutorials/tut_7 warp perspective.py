import cv2
import numpy as np

img = cv2.imread('Resources/blanca.png')

width, height = 250, 350
pts1 = np.float32([[111,219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

for x in range (0,4):
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 5, (0, 0, 255), 3)


cv2.imshow("original image", img)
cv2.imshow("Output image", imgOutput)
cv2.waitKey(0)

# this should work once the image used in the tutorial is found
