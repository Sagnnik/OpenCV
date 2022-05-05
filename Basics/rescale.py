import cv2 as cv

def rescaleFrame(frame, scale):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('OpenCV\Resources\Videos\dog.mp4')

while True:
    isTrue, frame=capture.read()

    frame_resize=rescaleFrame(frame, scale=0.5)

    cv.imshow('video', frame)

    cv.imshow('video2', frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()