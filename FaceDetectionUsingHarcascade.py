# Face detection is different from face recognition, 
# Face detection merely detects the presence of a face in an image
# Face recognition involves identifying whose face it is
#Face detection is usually performed using classifiers
#OpenCV comes with a lot of pre trained classifiers that we can use in any program
# 1> Har Cascaades, 2>Core Binary Patterns
# Har Cascades are really sensitive to noise in an image, it would detect something similar to face as face
# Har cascades are popular for detecting faces but not advanced
import cv2 as cv

# img = cv.imread("lady.jpg")
# img = cv.imread("group.jpg")
# img = cv.imread("group1.jpg")
img = cv.imread("group2.jpg")
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1)

print(f'Number of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y),(x+w,y+h), (0,255,0), thickness =2)

cv.imshow("detected faces", img)

cv.waitKey(0)