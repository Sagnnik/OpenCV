import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('OpenCV\Resources\Photos\cats.jpg')
cv.imshow('cats',img)

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)