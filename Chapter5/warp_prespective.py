import cv2 
import numpy as np

img = cv2.imread("reso/cards.jpeg")
width,height= 330,500
pts1 = np.float32([[(342,107)],[(438,95)],[(355,236)],[(465,225)]])
pts2 = np.float32([[(0,0)],[(width,0)],[(0,height)],[(width,height)]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image", img)
cv2.imshow("presective", imgOutput)

cv2.waitKey(0)