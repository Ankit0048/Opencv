import cv2
import numpy as np
from pyparsing import anyOpenTag

apple = cv2.imread('apple.jpg', -1)
orange = cv2.imread('orange.jpg', -1)

apple_copy = apple.copy()
orange_copy = orange.copy()

gaus_apple = [apple_copy]
gaus_orange = [orange_copy]

for i in range(5):
    gaus_apple.append(cv2.pyrDown(gaus_apple[-1]))
    gaus_orange.append(cv2.pyrDown(gaus_orange[-1]))

lp_apple = [gaus_apple[5]]
lp_orange = [gaus_orange[5]]

for i in range(5, 0, -1):
    lp_apple.append(cv2.subtract(gaus_apple[i-1], cv2.pyrUp(gaus_apple[i])))
    lp_orange.append(cv2.subtract(gaus_orange[i-1], cv2.pyrUp(gaus_orange[i])))

apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    lapalacian = np.hstack((apple_lap[:,0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(lapalacian)

apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow("merge", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
