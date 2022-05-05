import cv2 as cv
import numpy as np

img= cv.imread('OpenCV\Resources\Photos\cats.jpg')
cv.imshow('cats', img)

blank=np.zeros(img.shape, dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)

#ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY_INV)

canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)

contour,heirarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contour)} countours found')

cv.drawContours(blank,contour,-1,(0,0,255),1)
cv.imshow('contours',blank)

cv.waitKey(0)