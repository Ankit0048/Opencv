import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros([200,200, 3], np.uint8)
img= cv2.imread('lena.jpg', -1)

cv2.imshow("Image", img)
b, g, r = cv2.split(img)

plt.hist(b.ravel(), 256, [0, 256],color='blue', label='blue')
plt.hist(g.ravel(), 256, [0, 256],color='green', label='green')
plt.hist(r.ravel(), 256, [0, 256],color='red        ', label='red')
plt.show()                     

cv2.waitKey(0)
cv2.destroyAllWindows()