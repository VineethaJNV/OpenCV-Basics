import cv2 as cv

img = cv.imread("gettyimages-155096944-612x612.jpg")
cv.imshow("taj", img)

#Averaging
average = cv.blur(img,(3,3)) 
cv.imshow('Average Blur', average)

# Gaussian Blur
Gblur = cv.GaussianBlur(img,(3,3), 0 )
cv.imshow("gaussiain blur", Gblur)

# Median Blur => good at removing salt and pepper noise, not meant for kernel size greater than 3
median = cv.medianBlur(img, 3)
cv.imshow("median blur", median)

# Bilateral blurring => used in some advanced computer vision projects
#Applies blurring but retains edges in the image
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("bilateral blur", bilateral)





cv.waitKey(0)