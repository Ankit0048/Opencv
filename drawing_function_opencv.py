import cv2
import numpy as np

# img = cv2.imread('lena.jpg', -1)

img = np.zeros([512, 512, 3], np.uint8)

# img = cv2.line(img, (0,0), (255,255), (255,0,0), 3)
# img = cv2.arrowedLine(img, (0,0), (255,255), (255,0,0), 3)

# img = cv2.rectangle(img, (0,0), (255,255), (255,0,0), -1)
# img = cv2.circle(img, (255, 255), 50, (255,0,0), -1)
font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, "Beautiful", (50, 50), font, 1, (255, 255, 255), 1, cv2.LINE_AA)


cv2.imshow('line_on_Image',img)
cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()
