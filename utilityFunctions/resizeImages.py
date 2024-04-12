import cv2
import os
import myUtilities

width, height = 60, 60 # the new dimensions of the image
extension = '.png' # Change this to the extension you want to convert the image to
path = 'Replace with the directory in which the image exists'
changedImagesCounter = 0
for image in os.listdir(path): # note that when we loop over a directory, we are looping over the names of the files not the files themselves
    print(image) # THIS IS THE NAME OF THE IMAGE
    img = cv2.imread(path + '/' + str(image)) # after adding the image name to the path, we read the image itself
    # print(img.shape) # we can show its original shape
    # cv2.imshow("image", img) # we can show the image itself
    if True: #(image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".png")):
        outputImage = myUtilities.resizeImage(img, width, height) # resize the image
        os.remove(path + '/' + str(image)) # delete the original image from the containing folder
        # we assign each image a name and change the image type by simply changing its extension file and save it in the same dir.
        cv2.imwrite(path + '/' + str(changedImagesCounter) + extension, outputImage)
        changedImagesCounter += 1 # the counter which we use for naming the images
cv2.waitKey(0)
