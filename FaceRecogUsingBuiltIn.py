import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier("haar_face.xml")

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
p=[]
for i in os.listdir(r"C:\Users\33059\Desktop\OpenCV\jasmcaus opencv-course master Resources-Faces\train"):
    p.append(i)
print(p)

DIR = r"C:\Users\33059\Desktop\OpenCV\jasmcaus opencv-course master Resources-Faces\train"

features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread( img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 4)

            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label) # label is the list index
create_train()
print("Training done-------------------------")
features = np.array(features, dtype='object')
labels = np.array(labels)
print(f"the length of the features list = {len(features)}")
print(f"the length of the labels list = {len(labels)}")

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the recognizer on the features list and the lable list
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

