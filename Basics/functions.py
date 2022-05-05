import cv2 as cv

img=cv.imread('OpenCV\Resources\Photos\park.jpg')
#cv.imshow('park',img)

# Grayscale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

# Blur
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)

# Edge Cascade
canny=cv.Canny(blur, 125, 175)
cv.imshow('canny',canny)

# Dialation
dilated=cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dialte',dilated)

# Eroding
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('erode',eroded)

cv.waitKey(0)