import cv2 as cv
import numpy as np

# size of mask should be of same size as our image
img = cv.imread("jasmine.jpg")
cv.imshow("original", img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow("blank image", blank)

mask = cv.circle(blank, (img.shape[1]//2+15, img.shape[0]//2), 90, 255, -1)
cv.imshow("masked image", mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("masked image", masked)

cv.waitKey(0)