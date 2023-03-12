import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("gettyimages-155096944-612x612.jpg")
cv.imshow("taj", img)
# plt.imshow(img)
# plt.show()

#BGR => default in OpenCV => Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray taj", gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv taj", hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB taj", lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb taj", rgb)

#HSV to BGR
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("bgr from hsv", bgr)

#LAB to BGR
bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB --> HSV", bgr)

plt.imshow(rgb)
plt.show()
cv.waitKey(0)