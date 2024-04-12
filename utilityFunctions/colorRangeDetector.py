# This is a program to find the lower and upper bounds (in HSV format) of a color

import numpy as np
import cv2

# NOTE : RGB COLOR FORMAT IS MORE COMMONLY USED
# NOTE : OPENCV WORKS IN BGR BY DEFAULT
ColorInRGB = np.uint8([[[210, 4, 45]]]) # COLOR IN RGB FORMAT
# ColorInBGR = np.uint8([[[0,165,265]]]) # COLOR IN BGR FORMAT
# ColorInBGR = cv2.cvtColor(ColorInRGB, cv2.COLOR_RGB2BGR) # CONVERT IT FROM RGB TO BGR
ColorInHSV = cv2.cvtColor(ColorInRGB, cv2.COLOR_RGB2HSV) # CONVERT COLOR FROM BGR TO RGB

print("RGB Value:", ColorInRGB)
# print("BGR Value:", ColorInBGR)
print("HSV Value:", ColorInHSV)

# compute the lower and upper limits in HSV format
lowerLimit = ColorInHSV[0][0][0] - 10, 100, 100
upperLimit = ColorInHSV[0][0][0] + 10, 255, 255

# display the lower and upper limits
print("Lower Limit:", lowerLimit)
print("Upper Limit", upperLimit)

""" 
Usually, we can found the lower and upper limits of a color by a rough estimation
or we can use a color picker in which we keep trying the range which we want to detect 
"""
