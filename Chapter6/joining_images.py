import cv2 
import numpy as np

img = cv2.imread("reso/mine.jpg")

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Horiz",imgHor)
cv2.imshow("Vertical",imgVer)



cv2.waitKey(0)