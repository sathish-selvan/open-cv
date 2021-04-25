import cv2
import numpy as np

img = cv2.imread('reso/frnd.jpg')
kernal=np.ones((5,5),np.uint8)
#grey image or gray scale image
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),0)
#edge detector
imgCanny = cv2.Canny(img,150,200)
#increse the thickness of edges
imgDialation = cv2.dilate(imgCanny,kernal,iterations=3)
#erodes the dilated img 
imgEroded = cv2.erode(imgDialation,kernal,iterations=3)

cv2.imshow("grey img",imgGrey)
cv2.imshow("blur img",imgBlur)
cv2.imshow("canny img",imgCanny)
cv2.imshow("dialted img",imgDialation)
cv2.imshow("eroded img",imgEroded)
cv2.waitKey(0)