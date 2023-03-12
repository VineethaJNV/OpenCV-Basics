import cv2 as cv

#img = cv.imread("2023-02-15-09-44-10-639.jpg")
# cv.imshow("myself", img)
# # 1. Convert to gray scale
# gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("grayImage", gray_scale)
img = cv.imread("GettyImages-1208049833-scaled-e1654782377122.jpg")
cv.imshow("Taj", img)

# 1. Convert to gray scale
gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayTajImage", gray_scale)

# 2. Blur an image => removing the noise in an image
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("blurred image", blur)

# 3.Edge Cascade
canny = cv.Canny(img, 125, 175)
# canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

#4. Dilation
dilated = cv.dilate(canny, (7,7), iterations= 3)
cv.imshow("dilated edges", dilated)

#5. Eroded
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("eroded image", eroded)

#6. Resize
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)

#7.Cropping using array slicing
cropped = img[10:400, 300:500]
cv.imshow("cropped image", cropped)

cv.imshow("resized Taj",resized)


cv.waitKey(0)