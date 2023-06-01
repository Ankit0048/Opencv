import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', 0)
_, mask =  cv2.threshold(img, 220 ,255, cv2.THRESH_BINARY_INV)

kernal = np.ones([2,2], np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=2)

erossion = cv2.erode(mask, kernal, iterations=2)

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

images = [img, mask, dilation, erossion, opening, closing]
titles = ['IMAGE', 'MASKED', 'DILATED', 'ERODED', 'OPENING METHOD', 'CLOSING METHOD']

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show( )
