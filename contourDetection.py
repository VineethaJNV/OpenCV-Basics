import cv2 as cv
import numpy as np

image = cv.imread("gettyimages-155096944-612x612.jpg")
cv.imshow("Taj", image)

# img = cv.resize(image, (600,600))
# cv.imshow("chaamanthi", img)

blank = np.zeros(image.shape, dtype='uint8')
cv.imshow("blank", blank)

#convert to gray
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("gray Taj", gray)

#blur image
blur = cv.GaussianBlur(gray, (5,5),cv.BORDER_DEFAULT)
cv.imshow("blurred",blur)

#finding edges
canny = cv.Canny(image, 125, 175)
cv.imshow("edges", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("thresh imag", thresh)

#finding contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} are found')

cv.drawContours(blank, contours, -1, (0,0,255), 1 )
cv.imshow("contours drawn", blank)

cv.waitKey(0)