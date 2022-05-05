import serial
import cv2
import mediapipe as mp
import time

serialcomm= serial.Serial('COM7', 9600)
serialcomm.timeout= 1

tipIds= [4,8,12,16,20]

cx = 0
cy = 0
counter = 0


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False,
                          max_num_hands=2,
                          min_detection_confidence=0.5,
                          min_tracking_confidence=0.5)
    mpDraw = mp.solutions.drawing_utils

    pTime = 0
    cTime = 0

    while True:
        success, img = cap.read()
        img=cv2.resize(img, (1280,720))
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        lmList=[]
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    # print(id,lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id,cx,cy])
                    cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)

                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        
        fingers=[]
        if len(lmList)!=0:
            if lmList[tipIds[0]][1]> lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total=fingers.count(1)
            if total==0:
                # serialcomm.write('0'.encode())
                cv2.rectangle(img, (900,300), (1200,425), (0,255,0), thickness=8)
                cv2.putText(img, '0', (920,375), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 5)
            elif total==1:
                serialcomm.write('1'.encode())
                if results.multi_hand_landmarks:
                    for handLms in results.multi_hand_landmarks:
                        for id, lm in enumerate(handLms.landmark):
                            h, w, c = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            if(cx<480):
                                serialcomm.write('0'.encode())
                                print("Right")
                            else:
                                serialcomm.write('9'.encode())
                                print("left")
                
                cv2.rectangle(img, (900,300), (1200,425), (0,255,0), thickness=8)
                cv2.putText(img, '1', (920,375), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 5)
            elif total==2:
                serialcomm.write('2'.encode())
                if results.multi_hand_landmarks:
                    for handLms in results.multi_hand_landmarks:
                        for id, lm in enumerate(handLms.landmark):
                            h, w, c = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            if(cx<480):
                                serialcomm.write('0'.encode())
                                print("Right")
                            else:
                                serialcomm.write('9'.encode())
                                print("Left")
                
                cv2.rectangle(img, (900,300), (1200,425), (0,255,0), thickness=8)
                cv2.putText(img, '2', (920,375), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 5)
            elif total==3:
                serialcomm.write('3'.encode())
                if results.multi_hand_landmarks:
                    for handLms in results.multi_hand_landmarks:
                        for id, lm in enumerate(handLms.landmark):
                            h, w, c = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            if(cx<480):
                                serialcomm.write('0'.encode())
                                print("Right")
                            else:
                                serialcomm.write('9'.encode())
                                print("Left")
                
                cv2.rectangle(img, (900,300), (1200,425), (0,255,0), thickness=8)
                cv2.putText(img, '3', (920,375), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 5)

            elif total==4:
                #serialcomm.write('9'.encode())
                cv2.rectangle(img, (900,300), (1200,425), (0,255,0), thickness=8)
                cv2.putText(img, '4', (920,375), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 5)

            elif total==5:
                # serialcomm.write('5'.encode())
                cv2.rectangle(img, (900,300), (1200,425), (0,255,0), thickness=8)
                cv2.putText(img, '5', (920,375), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 5)


        flip_img = cv2.flip(img, 1)
        cv2.imshow("Image", flip_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
        	cap.release()
        	cv2.destroyAllWindows()
        	break
serialcomm.close()




