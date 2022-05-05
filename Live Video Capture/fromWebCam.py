import cv2 as cv

cap= cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while cap.isOpened():
    ret, frame= cap.read()
    frame= cv.flip(frame, 1)
    cv.imshow('Frame', frame)

    if cv.waitKey(1)== ord('q'):
        break

cap.release()
cv.destroyAllWindows()