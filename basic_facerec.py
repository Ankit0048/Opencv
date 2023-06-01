import cv2
import numpy as np
import face_recognition
import os


imgELon = face_recognition.load_image_file('Image_basic/elon_musk.jpg')
imgELon = cv2.cvtColor(imgELon, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('Image_basic/elon_test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgELon)[0]
print("***", faceLoc)
encodeElon = face_recognition.face_encodings(imgELon)[0]
cv2.rectangle(imgELon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 0), 1)

print(encodeElon)

faceLoc = face_recognition.face_locations(imgTest)[0]
print(faceLoc)
encodeTest= face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 0), 1)

list_encode = encodeElon.tolist()
string_encode = " ".join([str(x) for x in list_encode])
new_list = [float(x) for x in string_encode.split()]
new_array = np.ndarray(shape=(128,),buffer=np.array(new_list), dtype=np.float64)
array_1s = np.array(new_list)
print(new_array.shape)
print(encodeElon.shape)
print(encodeElon.itemsize)
print(encodeTest.shape)
results = face_recognition.compare_faces([array_1s],encodeTest)
faceDistance = face_recognition.face_distance([encodeElon], encodeTest)
print(results, faceDistance)


cv2.imshow("ELon Musk", imgELon)
cv2.imshow("ELon Test", imgTest)
cv2.waitKey(0)
cv2.destroyAllWindows()