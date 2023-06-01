import cv2
import datetime as dt

from cv2 import CAP_PROP_FRAME_HEIGHT
from cv2 import FONT_HERSHEY_SIMPLEX


cap = cv2.VideoCapture(0)
# four_cc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
# out = cv2.VideoWriter('my_first_vdo.avi', four_cc, 20.00, (640,480))

print(cap.isOpened())
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(3, 1280)
cap.set(4, 720)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # out.write(frame)
        text = "width : " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + " height : " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        date_time = str(dt.datetime.now())[0:-7]
        print(date_time)
        frame = cv2.putText(frame, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0 ,255 ,255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, date_time, (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0 ,255 ,255), 2, cv2.LINE_AA)

        cv2.imshow('VideoFrame', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()