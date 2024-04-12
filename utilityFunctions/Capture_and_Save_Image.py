import cv2
import os
import time

frameWidth = 640
frameHeight = 480


myPath = 'Replace this with the path to the folder where you want to save the images'
cameraNo = 1
cameraBrightness = 190
moduleVal = 10
minBlur = 100
grayImage = False
saveData = True
showImage = True
imgWidth = frameWidth
imgHeight = frameHeight

global countFolder
cap = cv2.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, cameraBrightness)

count = 0
countSave = 0

def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(myPath + str(countFolder)):
        countFolder = countFolder + 1
    os.makedirs(myPath + str(countFolder)) # our directories have the form: collectedImages + folder number

if saveData:
	saveDataFunc()

while True:

    success, img = cap.read()
    img = cv2.resize(img, (imgWidth, imgHeight))
    if grayImage:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if saveData:
        blur = cv2.Laplacian(img, cv2.CV_64F).var()
        if count % moduleVal == 0:#and blur > minBlur:
            nowTime = time.time()
            cv2.imwrite(myPath + str(countFolder) + '/' + str(countSave) + "_" + str(int(blur)) + "_" +str(nowTime) + ".png", img)
            countSave += 1
        count += 1
        print(count)
        print(countSave)


    if showImage:
        cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
