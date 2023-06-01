import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
# print(img.shape)
# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball
# cv2.imshow('newimage', img)

img2 = cv2.imread('opencv-logo.png')
img = cv2.resize(img, (600, 794))
print(img.shape)
print(img2.shape)
img3 = cv2.add(img, img2)
# img3 = cv2.addWeighted(img, 0.6, img2, 0.4, 0)

cv2.imshow('oldimage', img3)
cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()