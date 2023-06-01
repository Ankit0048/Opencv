import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('crackedwall.jpg', -1)

canny = cv2.Canny(img, 100, 200)
images = [img, canny]
title = ['Image', 'Canny']

for i in range(2):
    plt.subplot(1, 2,  i+1)
    plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()