import cv2

def click_event(event, x, y, flags, params):

    if event== cv2.EVENT_LBUTTONDBLCLK :
        print(x,', ', y)
        cv2.putText(img, str(x)+', '+str(y), (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 2)
        cv2.imshow('frame',img)

    if event== cv2.EVENT_RBUTTONDBLCLK :
        print(x,', ',y)
        font= cv2.FONT_HERSHEY_COMPLEX_SMALL
        b=img[x,y,0]
        g=img[x,y,1]
        r=img[x,y,2]
        cv2.putText(img, str(b)+' '+str(g)+' '+str(r), (x,y), font, 1, (255,255,0), thickness=2)
        cv2.imshow('frame', img)

if __name__ == "__main__":
    img=cv2.imread('OpenCV\Resources\Photos\cats.jpg', 1)
    cv2.imshow('frame', img)
    cv2.setMouseCallback('frame', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

