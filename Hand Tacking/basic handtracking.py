import cv2 as cv
import mediapipe as mp
import time

cap= cv.VideoCapture(0)

mphands= mp.solutions.hands
hands= mphands.Hands()
mpDraw= mp.solutions.drawing_utils


ptime=0
ctime=0

while True:
    success,img= cap.read()
    imgRGB= cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results= hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    #cv.imshow("image",img)
    #cv.waitKey(1)

    if results.multi_hand_landmarks:
       for handlms in results.multi_hand_landmarks:
           for id,lm in enumerate(handlms.landmark):
               #print(id,lm)
               h,w,c= img.shape
               cx,cy= int(lm.x*w), int(lm.y*h)
               print(id,cx,cy)
               if id==6:
                   cv.circle(img,(cx,cy),10,(255,40,140),5)
           mpDraw.draw_landmarks(img,handlms,mphands.HAND_CONNECTIONS)

    ctime=time.time()
    fps= 1/(ctime-ptime)
    ptime= ctime

    cv.putText(img,str(int(fps)),(10,70) ,cv.FONT_HERSHEY_PLAIN,4,(0,255,0),3)

    cv.imshow("image",img)
    cv.waitKey(1)