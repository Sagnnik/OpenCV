import cv2 as cv
# img=cv.imread('OpenCV\Resources\Photos\cat_large.jpg')

# cv.imshow('cat',img)

# reading videos

capture=cv.VideoCapture('OpenCv\Resources\Videos\dog.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()