import cv2

#READING AN IMAGE
#img = cv2.imread("Resources/blanca.png")
#cv2.imshow("Blanca", img)
#print(img.shape) # returns(height, width, number of channels) of img, where height and width are in pixels
#cv2.waitKey(0) # amount to wait in ms, special case : 0 for indefinite display

frameWidth = 640
frameHeight = 480

#READING FROM A SAVED VIDEO

cap = cv2.VideoCapture("Resources/mallak.mp4") # video can be an mp4 file or a webcam import
while True: # we declare a loop from which we read each frame of the video
   success, img = cap.read() # it reads from cap a frame and stores it in img, yielding true in success if frame is successfully captured, else yielding false
   img = cv2.resize(img, (frameWidth, frameHeight))
   cv2.imshow("Mallak", img)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
       # note that this will give an error when there are no more frames to be captured

#READING FROM WEBCAM

# NOTE: The frame width and height supplied should among the resolutions supported by the camera
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0) # 0 for first webcam, and 1 for second webcam(if exists), etc..
# cap.set(3, frameWidth) # 3 is a number set by the library creators to indicate the width
# cap.set(4, frameHeight) # 4 is a number set by the library creators to indicate the height
# while True:
#     success, img = cap.read()
#     cv2.imshow("My camera", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
