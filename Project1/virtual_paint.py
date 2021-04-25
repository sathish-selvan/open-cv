import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,720)
cap.set(4,640)
cap.set(10,100)

myColours = [[106,129,95,125,190,255]]


myPoints = []
def findColor(img,myColours):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower=np.array(myColours[0][0:3])
    upper=np.array(myColours[0][3:6])
    mask = cv2.inRange(imgHSV,lower,upper)
    x,y = getContours(mask)
    cv2.circle(imgContour,(x,y),10,(255,0,0),cv2.FILLED)
    if x!=0 and y!=0:
        myPoints.append([x,y])
    drawOnCanvas(myPoints)
    #cv2.imshow("out",mask)

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,h,w = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if area > 100:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints):
    for points in myPoints:
        cv2.circle(imgContour,(points[0],points[1]),10,(255,0,0),cv2.FILLED)

while True:
    success, img = cap.read()
    imgContour=img.copy()
    findColor(img,myColours)
    
    cv2.imshow("Vedio",imgContour)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()