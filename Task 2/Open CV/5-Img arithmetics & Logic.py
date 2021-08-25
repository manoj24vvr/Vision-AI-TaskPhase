import numpy as np
import cv2

img1 = cv2.imread('5-1.png')
img2 = cv2.imread('5-3.png')
#img2 = cv2.imread('5-2.png')

#add = img1 + img2
# Adds the BGR values of both pics to get final pic.
#add = cv2.add(img1,img2)
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.imshow('m_i', mask_inv)
cv2.imshow('1', img1_bg)
cv2.imshow('2',img2_fg)
cv2.imshow('dst', dst)
#cv2.imshow('add',weighted)
#cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()