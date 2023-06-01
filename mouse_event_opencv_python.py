import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


def click_Event (event, x, y, flags,  param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , ' + str(y)
        cv2.putText(img, strXY, (x,y), font, 1, (255,255,255), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y][x][0]       
        g = img[y][x][1]       
        r = img[y][x][2]       
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(r) + " , " + str(g) + " , " +str(b)
        cv2.putText(img, text, (x, y), font, 1, (255, 0 , 255), 2)
        cv2.imshow('image', img)


while True:
    # img = np.zeros([512, 512, 3], np.uint8)
    img = cv2.imread('lena.jpg')
    cv2.imshow('image', img)

    print("Information")

    cv2.setMouseCallback('image', click_Event)
    if cv2.waitKey(0) == ord('q'):
        break

cv2.destroyAllWindows()
