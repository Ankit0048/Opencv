import cv2
import numpy as np

img = cv2.imread('gradient.png')

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('IMAGE', img)

cv2.imshow('BINARY', th1)
cv2.imshow('BINARY INV', th2)
cv2.imshow('TRUNC', th3)
cv2.imshow('ZERO', th4)
cv2.imshow('ZERO INV', th5)

cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()