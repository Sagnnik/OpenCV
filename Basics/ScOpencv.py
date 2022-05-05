import cv2 as cv
import pyautogui
import numpy as np
import imutils

for x in range(1,3):
    # taking screenshot
    img= pyautogui.screenshot()
    img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
    cv.imwrite(f"C:/Users/USER/OneDrive/Documents/VSCode/SCfiles/Sc_to_disk{x}.png", img)

# #displaying screenshot
# image=cv.imread("Sc_to_disk.png")
# cv.imshow('Frame', imutils.resize(image, width=600))
# cv.waitKey(0)