import cv2 as cv
import numpy as np

#Thresholding is binarizing the image based on a range => either black or white
img = cv.imread("jasmine.jpg")
cv.imshow("original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
#threshold has the integer value
#thresh is the binarized image
cv.imshow("simple thresholded", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple inverse thresholded", thresh_inv)

# Adaptive threshold => Computer finds the optimal threshold value by itself through mean
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
# 3 is the c value, which will be subtracted from mean to fine tune the threshold
cv.imshow("Adaptive threshold", adaptive_thresh)

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adaptive threshold", adaptive_thresh_gaussian)



cv.waitKey(0)
