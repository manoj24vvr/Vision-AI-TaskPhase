import numpy as np
import cv2
from numpy.lib.function_base import median

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    #hsv hue saturation value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([161,155,84])
    upper_red = np.array([179,255,255])

    lower_blue = np.array([94,80,2])
    upper_blue = np.array([130,255,255])

    lower_green = np.array([25,52,72])
    upper_green = np.array([102,255,255])
    # To every color except white
    low = np.array([0,42,0])
    high = np.array([179,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)

    blur = cv2.GaussianBlur(res, (15,5),0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 7, 75)


    cv2.imshow('frame', frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res', res)
    #cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF('q')
    if k == 5 or k == 'q':
        break

cv2.destroyAllWindows()
cap.release()