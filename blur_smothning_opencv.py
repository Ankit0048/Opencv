import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', -1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# _, mask =  cv2.threshold(img, 220 ,255, cv2.THRESH_BINARY_INV)

kernal = np.ones([5,5], np.float32)/25
dst = cv2.filter2D(img,-1, kernal)

blur = cv2.blur(img, (5,5))

gaussian = cv2.GaussianBlur(img, (5,5), 0)

median = cv2.medianBlur(img, 5)

bilateral = cv2.bilateralFilter(img, 9, 75, 75)
images = [img, dst, blur, gaussian, median, bilateral]
titles = ['IMAGE', "Homogenous", 'Blur', 'Gaussian', 'Median', 'Bilateral']

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show( )
