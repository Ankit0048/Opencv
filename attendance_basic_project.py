import cv2
import numpy as np
import face_recognition
import os

from datetime import datetime


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeList.append(face_recognition.face_encodings(img)[0])
    return encodeList


def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


path = "Image_basic"
images = []
classname = []
mylist = os.listdir(path)
print(mylist) 

for cl in mylist:
    currImg = cv2.imread(path+'/'+cl)
    images.append(currImg)
    classname.append(cl.strip('.jpg'))
print(classname)

encodeListKnown = findEncodings(images)
print("Encoding Complete")
# print(encodeListKnown)
print(encodeListKnown[0])
# encoding1 = encodeListKnown[0].tolist()
# print(encoding1)
# string_encoding1 = " ".join([str(x) for x in encoding1])
# print(string_encoding1)
# recheck_encoding1 = np.array([float(x) for x in string_encoding1.split()])
# print(recheck_encoding1==encodeListKnown[0])
s = face_recognition.compare_faces(encodeListKnown[0], encodeListKnown[0])
print(s)
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     success, img = cap.read()
#     imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

#     faceCurrFrame = face_recognition.face_locations(imgS)
#     endcodesCurrFrame = face_recognition.face_encodings(imgS, faceCurrFrame)

#     print(faceCurrFrame)

#     for encodeFace, faceLoc in zip(endcodesCurrFrame, faceCurrFrame):
#         matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
#         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#         print(faceDis)
#         matchIndex = np.argmin(faceDis)

#         if matches[matchIndex]:
#             name = classname[matchIndex].upper()
#             print(name)
#             y1, x2, y2, x1 = faceLoc
#             y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4 
#             cv2.rectangle(img, (x1, y1), (x2,y2), (0, 255, 0), 1)
#             cv2.putText(img, name,(x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255,255), 2)
#             markAttendance(name)

#     cv2.imshow("Webcam", img)
#     cv2.waitKey(1)


    
# faceLoc = face_recognition.face_locations(imgELon)[0]
# encodeElon = face_recognition.face_encodings(imgELon)[0]
# cv2.rectangle(imgELon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 0), 1)

# faceLoc = face_recognition.face_locations(imgTest)[0]
# encodeTest= face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 0), 1)

# results = face_recognition.compare_faces([encodeElon],encodeTest)