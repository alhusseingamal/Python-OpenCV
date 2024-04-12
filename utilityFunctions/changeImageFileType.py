
import cv2
import os
import myUtilities


extension = '.png' # Change this to the extension you want to convert the image to
path = 'Enter your path here'
# for image in os.listdir(path):
image = 'Replace this with the name of the image you want to convert to png format'
print(image) # show the image

img = cv2.imread(path + '/' + str(image))
if image.endswith(".webp"):
    outputImage = img
    # os.remove(path + '/' + str(image))
    cv2.imwrite(path + '/' + str(image) + extension, outputImage)
cv2.waitKey(0)
