import cv2
import numpy as np

widthImg = 640
heightImg = 480

cap = cv2.VideoCapture(0)
cap.set(3,widthImg)
cap.set(4,heightImg)
cap.set(10,100)

def getContours(img):
    biggest = np.array([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if area > 5000:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            
            objCor = len(approx)
            maxArea = 5000
            if objCor == 4  and area > maxArea :
                
                biggest = approx
                maxArea = area
    #cv2.drawContours(imgContour,biggest,-1,(255,0,0),20)
    return biggest

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(1,1),1)
    imgCanny = cv2.Canny(imgGray,200,70)
    kernal = np.ones((3,3))
    imgDilate = cv2.dilate(imgCanny,kernal,iterations=3)
    imgErode = cv2.erode(imgDilate,kernal,iterations=1)
    return imgErode

def recorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    print(myPointsNew)
    return myPointsNew
def getWarp(img,biggest):
    newPoints=recorder(biggest)
    pts1 = np.float32(newPoints)
    pts2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])

    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(img,matrix,(widthImg,heightImg))
    return imgOutput

while True:
    sucsess,img = cap.read()
    
    cv2.resize(img,(widthImg,heightImg))
    imgContour = img.copy()
    imgThresh=preProcessing(img)
    biggest=getContours(imgThresh)
    imgOutput = getWarp(img,biggest)
    cv2.imshow("Doc scaner",imgThresh)
    cv2.imshow("Doc scaner",imgOutput)
    print(biggest)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

