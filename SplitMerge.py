import cv2 as cv
import numpy as np

img = cv.imread("muddamanadaaram.jpg")
cv.imshow("flower",img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

#split an image into color channels
b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
# cv.imshow("blue", b)
# cv.imshow("green", g)
# cv.imshow("red", r)
cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge the color channels into an image
merged = cv.merge([b,g,r])
cv.imshow("merged image", merged)

cv.waitKey(0)