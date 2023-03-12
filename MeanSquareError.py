import cv2 as cv
import numpy as np
import imutils

img1 = cv.imread("jasmine.jpg")
img2 = cv.imread("jasmineedited.jpg")

#converting into gray scale
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

def mean_square_error(img1, img2):
    h,w = img1.shape
    diff = cv.subtract(img1, img2)
    error = np.sum(diff**2)
    mse = error/(float(h*w))
    return mse

error = mean_square_error(gray1, gray2)
print("Image matching error between the two images is:",error)

#Absolute difference
image1 = cv.imread("Screenshot (168).png")
image2 = cv.imread("Screenshot (169).png")
# cv.imshow("original image", image1)
# cv.imshow("edited image",image2)
# image1 = cv.imread("jasmine.jpg")
# image2 = cv.imread("jasmineedited.jpg")

image1 = imutils.resize(image1, height = 600)
image2 = imutils.resize(image2, height = 600)

diff = image1.copy()
cv.absdiff(image1, image2, diff)
cv.imshow("Absolute difference", diff)

#convert the difference into grayscale
diff_gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

#increasing the size of the diffeences
for i in range(0,3):
    dilated = cv.dilate(diff_gray.copy(), None, iterations = i+ 1)

(T, thresh) = cv.threshold(dilated, 3, 255, cv.THRESH_BINARY)

#Find contours in the binarized image
contours = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

for c in contours:
    (x,y,w,h) = cv.boundingRect(c)
    cv.rectangle(image2, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imwrite("differences.png", image2)
differences = cv.imread("differences.png")
cv.imshow("differences",differences)

cv.waitKey(0)
cv.destroyAllWindows()

