import face_recognition
import numpy as py
import cv2


img1 = face_recognition.load_image_file('kevin1.JPG')
img2 = face_recognition.load_image_file('kevin2.JPG')
img3 = face_recognition.load_image_file('kevin3.JPG')
notImg4 = face_recognition.load_image_file('notKevin.JPG')

img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
img4 = cv2.cvtColor(img4,cv2.COLOR_BGR2RGB)

encodeImg1 = face_recognition.face_encodings(img1)[0]
encodeImg2 = face_recognition.face_encodings(img2)[0]
encodeImg3 = face_recognition.face_encodings(img3)[0]
encodeImg4 = face_recognition.face_encodings(img4)[0]

result1 = face_recognition.compare_faces([encodeImg1],encodeImg1);
result2 = face_recognition.compare_faces([encodeImg1],encodeImg2);
result3 = face_recognition.compare_faces([encodeImg1],encodeImg3);
result3 = face_recognition.compare_faces([encodeImg1],encodeImg4);
print(result1)
print(result2)
print(result3)
print(result3)#false



#this is og image
#imgS = face_recognition.load_image_file('kevin1.JPG')
#imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
#
#faceloc = face_recognition.face_locations(imgS)[0]
#encodeSelena = face_recognition.face_encodings(imgS)[0]
#print(encodeSelena)
#cv2.rectangle(imgS,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(225,0,225),2)

# print(encodeSelena)

#this is test image
#imgSt = face_recognition.load_image_file('kevin2.JPG')
#imgSt = cv2.cvtColor(imgSt,cv2.COLOR_BGR2RGB)

#faceloc1 = face_recognition.face_locations(imgSt)[0]
#encodeSelena_test = face_recognition.face_encodings(imgSt)[0]
#cv2.rectangle(imgSt,(faceloc1[3],faceloc1[0]),(faceloc1[1],faceloc1[2]),(225,0,225),2)

#test image 3 for false comparision
#img3 = face_recognition.load_image_file('kevin3.JPG')
#img3 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

#faceTloc = face_recognition.face_locations(img3)[0]
#encodeTest = face_recognition.face_encodings(img3)[0]
#cv2.rectangle(img3,(faceTloc[3],faceTloc[0]),(faceTloc[1],faceTloc[2]),(225,225,0),0)



#this part is comparision and calculating face distance
#result = face_recognition.compare_faces([encodeSelena,encodeTest], encodeSelena_test)
#faceDis = face_recognition.face_distance([encodeSelena,encodeTest],encodeSelena_test)
#print(result,faceDis)

#cv2.putText(imgSt,f'{result}{round(faceDis[0],4)}{round(faceDis[1],4)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

# display images and outline

#cv2.imshow('selena',imgS)
#cv2.imshow('selena_test',imgSt)
#cv2.imshow('test image ',img1)


#cv2.waitKey(0)