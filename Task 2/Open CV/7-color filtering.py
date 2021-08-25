import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    #hsv hue saturation value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    lower_red = np.array([100,100,100])
    upper_red = np.array([255,255,180])

    dark_red = np.uint8([[[12,22,121]]])
    dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()