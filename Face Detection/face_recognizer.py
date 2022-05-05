import cv2 as cv
import numpy as np
import os

DIR=r'C:\Users\USER\OneDrive\Documents\VSCode\OpenCV\Resources\Faces\train'

#Starting the Haar Casacde object
haar_cascade=cv.CascadeClassifier(r'C:\Users\USER\OneDrive\Documents\VSCode\haar_face.xml')

people=[]
for i in os.listdir(DIR):
    people.append(i)

#Starting the Face Recognier
face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\Users\USER\OneDrive\Documents\VSCode\face_trained.yml')

#Reading the img
img=cv.imread(r'C:\Users\USER\OneDrive\Documents\VSCode\OpenCV\Resources\Faces\val\mindy_kaling\3.jpg')

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

faces_rect=haar_cascade.detectMultiScale(gray,1.1,6)

for (x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+w]

    #Prediction by the recognizer
    label,confidence=face_recognizer.predict(faces_roi)

    print(f'Label= {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]),(20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,0,0), thickness=2)
    cv.rectangle(img,(x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detceted Face', img)

cv.waitKey(0)