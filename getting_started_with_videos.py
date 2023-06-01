import cv2
from cv2 import CAP_PROP_FRAME_HEIGHT

cap = cv2.VideoCapture(0)
four_cc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('my_first_vdo.avi', four_cc, 20.00, (640,480))

print(cap.isOpened())
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))


while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        out.write(frame)

        cv2.imshow('VideoFrame', gray   )
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()