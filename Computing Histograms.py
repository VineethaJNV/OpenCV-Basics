import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#helps in analyzing, equalizing the image  so that there is no peeking of pixel values
img = cv.imread("jasmine.jpg")
cv.imshow("taj", img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask= circle)
cv.imshow("mask", mask)

#Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

gray_hist_mask = cv.calcHist([gray], [0], mask, [256], [0, 256])

# plt.figure(0)
# plt.title('Grayscale Histogram')
# plt.xlabel('bins')
# plt.ylabel('number of pixles')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show() 

# plt.figure(1)
# plt.title('Grayscale Masked Histogram')
# plt.xlabel('bins')
# plt.ylabel('number of pixles')
# plt.plot(gray_hist_mask)
# plt.xlim([0,256])
# plt.show() 

#Histogram of a color image
plt.figure(2)
plt.title('Color Histogram')
plt.xlabel('bins')
plt.ylabel('number of pixles')

colors = ('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
plt.show() 


cv.waitKey(0)