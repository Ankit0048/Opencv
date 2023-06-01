import cv2
import numpy as np

img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

bitwise_Or = cv2.bitwise_or(img1, img2)
bitwise_Xor = cv2.bitwise_xor(img1, img2)
bitwise_Not1 = cv2.bitwise_not(img1)
bitwise_Not2 = cv2.bitwise_not(img2)
bitwise_And = cv2.bitwise_and(img1, img2)

cv2.imshow('OR', bitwise_Or)
cv2.imshow('AND', bitwise_And)
cv2.imshow('XOR', bitwise_Xor)
cv2.imshow('NOT1', bitwise_Not1)
cv2.imshow('NOT2', bitwise_Not2)
