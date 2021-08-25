import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.png',cv2.IMREAD_UNCHANGED)
#IMREAD_COLOR - 1
#IMREAD_UNCHANGED - -1
#IMREAD_GRAYSCALE - 0

cv2.imshow('watch.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##plt.imshow(img, cmap = 'gray',interpolation = 'bicubic')
##plt.xticks([]),plt.yticks([])  # to hide tick values on X and Y axis
##plt.plot([50,100,150],[80,100,160],'c',linewidth = 5)
##plt.show()

cv2.imwrite('watchgray.png',img)

