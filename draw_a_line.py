# put two points and it will join those points and it will be visible  as a line
import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


def click_Event (event, x, y, flags,  param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (255, 255, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], (255,255,255), 2, cv2.LINE_AA)
        cv2.imshow('image', img)
    


while True:
    points = []
    img = np.zeros([720, 1366, 3], np.uint8)
    # img = cv2.imread('lena.jpg')
    cv2.imshow('image', img)

    print("Information")

    cv2.setMouseCallback('image', click_Event)
    if cv2.waitKey(0) == ord('q'):
        break

cv2.destroyAllWindows()