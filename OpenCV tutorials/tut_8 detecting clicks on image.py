import cv2
import numpy as np

circles = np.zeros((4, 2), int) #(4,2) for 4 points each with x and y
counter = 0
def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter >= 4:
            return
        circles[counter] = x, y
        counter = counter + 1
        print(circles)

img = cv2.imread("Resources/book.jpg")

while True:
    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("output image", imgOutput)
    elif counter >= 4:
        break

    for x in range (0,4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 5, (0, 0, 255), 3)

    cv2.imshow("Blanca", img)
    cv2.setMouseCallback("Blanca", mousePoints)
    # cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
