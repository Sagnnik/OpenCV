import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank',blank)

# Drawing a Rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2 , blank.shape[0]//2),(0,255,0),thickness=-1)
#cv.imshow('rect',blank)

# Drawing a Circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),50,(0,0,255) ,thickness=-1)
#cv.imshow('circle',blank)

# Drawing a Line
cv.line(blank,(100,250),(200,400),(255,255,255),thickness=5)
#cv.imshow('line',blank)

# Write text on an img
cv.putText(blank,'Hello, I am Sagnnik',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0, (255,0,0), thickness=3)
#cv.imshow('Text',blank)

cv.waitKey(0)