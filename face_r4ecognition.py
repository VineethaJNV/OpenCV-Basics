import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier("haar_face.xml")

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# features = np.load('features.npy')
# lables = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\33059\Desktop\OpenCV\jasmcaus opencv-course master Resources-Faces\val\ben_afflek\4.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)

#Detect the faces in the image
faces_rect  = haar_cascade.detectMultiScale(gray, 1.1, 4)

for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence} ')

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness = 2)
cv.imshow("detected", img)

cv.waitKey(0)