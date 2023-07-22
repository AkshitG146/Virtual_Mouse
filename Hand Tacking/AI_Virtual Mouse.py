import cv2 as cv
import pyautogui as pg
import mediapipe as mp

cap= cv.VideoCapture(0)
hand_detector= mp.solutions.hands.Hands()
screen_width, screen_height = pg.size()
index_y=0

drawing_utils = mp.solutions.drawing_utils
while True:
    success,frame= cap.read()
    frame= cv.flip(frame,1)
    rgb_frame= cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results= hand_detector.process(rgb_frame)
    hands= results.multi_hand_landmarks
    #print(hands)
    if hands:
        for hand in hands:
          #drawing_utils.draw_landmarks(frame, hand)
          for id, landmark in enumerate(hand.landmark):
            h,w,c= frame.shape
            cx= int(landmark.x*w)
            cy= int(landmark.y *h)
            #print(cx,cy)
            if id==8:
                cv.circle(frame,(cx,cy),10,(255,0,0),2)
                index_x = screen_width/w*cx
                index_y = screen_height/h*cy
                
            if id==4:
                cv.circle(frame,(cx,cy),10,(255,0,0),2)
                thumb_x = screen_width/w*cx
                thumb_y = screen_height/h*cy
                print('outside', abs(index_y - thumb_y))
                if abs(index_y - thumb_y) < 25:
                        pg.click()
                        pg.sleep(1)
                elif abs(index_y - thumb_y)<100:
                        pg.moveTo(index_x, index_y)  
    cv.imshow('Virtual Mouse',frame)
    cv.waitKey(1)
