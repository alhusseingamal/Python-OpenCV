import cv2

# in CV, +ve x is to the east, and +ve y is to the south

path = "Resources/img1.PNG"
width, height = 400, 400

img = cv2.imread(path)
imgResized = cv2.resize(img, (width, height))
# since the image itself is a matrix, all we do is we specify a paricular part (submatrix) of the image that we want
# the remaining part is cropped
imgCropped = imgResized[100:height, 0:width] # we removed the first 100 rows of the height and took the full width

imgCroppedResized = cv2.resize(imgCropped, (img.shape[1], img.shape[0])) # cropped image is resized to size of original image

print(imgResized.shape) # (height, width, number of channels; 3 for BGR)
#cv2.imshow("img", img)
#cv2.imshow("img resized", imgResized)
#cv2.imshow("img resized and Cropped", imgCropped)
cv2.imshow("img Cropped is resized", imgCroppedResized)
cv2.waitKey(0)



