import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=1) as hands:
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS, 
                                          mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=4), 
                                          mp_drawing.DrawingSpec(color=(255,0,0), thickness=2, circle_radius=2)) 

            for hand_landmarks in results.multi_hand_landmarks:
                index_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * 640)
                index_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * 480)
                thumb_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * 640)
                thumb_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * 480)
            
            distance = math.sqrt((index_x - thumb_x)**2 + (index_y - thumb_y)**2)
            midpoint_x = int((index_x + thumb_x)/2)
            midpoint_y = int((index_y + thumb_y)/2)  
            
            cv2.circle(frame, (index_x, index_y), 10, (0,0,255), thickness=10)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0,0,255), thickness=10)
            cv2.line(frame, (index_x, index_y), (thumb_x, thumb_y), (0,0,255), thickness=10)
            cv2.circle(frame, (midpoint_x, midpoint_y), 10, (0,255,255), thickness=10)
            
            pyautogui.moveTo(midpoint_x*3, midpoint_y*2.25)
            if (distance < 30):
                pyautogui.click(index_x*3, index_y*2.25)
                time.sleep(1)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()