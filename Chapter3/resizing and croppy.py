import cv2
import numpy as np

img = cv2.imread("reso/mine.jpg")
print(img.shape)

imgResize = cv2.resize(img,(300,300))

imgCropped = img[0:500,0:500]
cv2.imshow("image",img)
cv2.imshow("resized",imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)