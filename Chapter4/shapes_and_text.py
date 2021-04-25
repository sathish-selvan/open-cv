import cv2
import numpy as np

img = np.zeros((512,512,3))

#img[200:400,300:400] = 255,0,0
cv2.line(img,(0,0),(512,512),(0,255,0),3)
cv2.rectangle(img,(0,0),(300,200),(200,0,0),cv2.FILLED)
cv2.circle(img,(200,200),30,(255,255,0),5)

cv2.putText(img,"OPEN CV",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)


cv2.imshow("black img",img)


cv2.waitKey(0)