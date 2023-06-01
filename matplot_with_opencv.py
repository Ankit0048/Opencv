import cv2
from matplotlib import pyplot as plt


img = cv2.imread('lena.jpg')
cv2.imshow("Image", img)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img2)
plt.xticks([])
plt.yticks([])
plt.show()

cv2.waitkey(0)
cv2.destroyAllWindows()