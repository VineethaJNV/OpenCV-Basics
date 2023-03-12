import cv2 as cv
import numpy as np

img = cv.imread("gettyimages-155096944-612x612.jpg")
cv.imshow("image",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray scale", gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

#Sobel gradient magnitude representation
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobelY)
cv.imshow("sobelX", sobelx)
cv.imshow("sobelY", sobelY)
cv.imshow("combined sobel", combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow("canny", canny)


cv.waitKey(0)
