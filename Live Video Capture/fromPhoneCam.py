import cv2 as cv

cap=cv.VideoCapture('http://192.168.62.128:8080/video')

while cap.isOpened():
    ret, frame= cap.read()
    cv.imshow('Frame', frame)

    if cv.waitKey(1)== ord('q'):
        break

cap.release()
cv.destroyAllWindows()