import cv2
import numpy as np

# NOTE: BGR stands for BLUE-GREEN-RED
# When we specify the color of an image using a 3-channel BGR like (b,g,r)
# each letter corresponds to the intensity of the component of the corresponding color

img = np.zeros((512, 512, 3), np.uint8)
# if we don't add the 3(BGR), we get a one-channel image; black or white or some shade of greyscale
print(img.shape)
print(img)
# CHANGING THE COLOR OF AN IMAGE
#img[0:122, :] = 255, 0, 0 # make the first 122 rows of height, and the full of width of 1st channel = 255, 2nd and 3rd channels to 0; this is the blue color
# img[:] to select the whole image; all rows and all columns

# CREATING A LINE
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)
cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (150, 400), 50, (255, 0, 0), 3)
cv2.putText(img, "Draw Shapes", (75, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
# line(image, point 1, point 2, color, thickness)
# rectangle(image, upperleft point, lowerright point, color, thickness)
cv2.imshow("Image", img)
cv2.waitKey(0)
