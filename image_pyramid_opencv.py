import cv2
import numpy as np

img = cv2.imread('lena.jpg', -1)

layer = img.copy()

text = 'L1'
cv2.imshow(text,layer)

gaussian_pyramid = [layer]
for i in range(5):
    gaussian_pyramid.append(cv2.pyrDown(gaussian_pyramid[-1]))
    # cv2.imshow(text + str(i+1), gaussian_pyramid[-1])

layer = gaussian_pyramid[5]
cv2.imshow('Upperlevel of gaussian pyramid', layer)
laplacian_pyramid = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid[i])
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_extended)
    laplacian_pyramid.append(laplacian)
    cv2.imshow(text + str(i+1),laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()