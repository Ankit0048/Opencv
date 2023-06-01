import cv2
import numpy as np

img = cv2.imread('pic2.png', -1)

img_copy = img.copy()

img_gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray,170,250, cv2.THRESH_BINARY)
thresh = cv2.medianBlur(thresh,9)
contours, _ = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0,0,0), 1)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectratio = float(w)/h
        if aspectratio >= 0.95 and aspectratio <= 1.05:
            cv2.putText(img,'Square', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0), 1)
        else:
            cv2.putText(img,'Rectangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0), 1)
    else:
        cv2.putText(img,'Circle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0), 1)
        
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
