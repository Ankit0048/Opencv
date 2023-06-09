import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('sudoku.png', cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint0(np.absolute(lap))

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelc = cv2.bitwise_or(sobely, sobelx)

images = [img, lap, sobelx, sobely, sobelc]
title = ['Image', 'Lapalacian', 'sobelX', 'sobelY', 'SobelCombined']

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()