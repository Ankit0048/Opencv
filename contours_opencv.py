import cv2
import numpy as np

img = cv2.imread('opencv-logo.png',-1)

img_copy = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

img_contour = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow('Countour', img_contour)
cv2.imshow('Image', img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()

