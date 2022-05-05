import cv2 as cv
import numpy as np

img=cv.imread('OpenCV/Resources/Photos/group 1.jpg')
cv.imshow('face', img)

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade= cv.CascadeClassifier('C:/Users/USER/OneDrive/Documents/VSCode/haar_face.xml')

face_rect=haar_cascade.detectMultiScale(gray,1.1,1)

print(face_rect)
print(type(face_rect))
print(f'Number of Faces detected= {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0), thickness=2)

cv.imshow('face detect',img)

cv.waitKey(0)