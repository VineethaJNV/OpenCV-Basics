import cv2 as cv
import numpy as np

img = cv.imread("LinkedinProfile.png")
cv.imshow("flower image", img)

#Translation

def translate(img, x, y): #x and y are the no of pixels to translate
    transMat = np.float32([[1,0,x],[0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x => Left
# +x => right
# -y => down
# +y => up
# translated = translate(img, 100, 100)
# translated = translate(img, -100, 100)
translated = translate(img, 100, -100)
cv.imshow("translated", translated)

#Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle , 1.0)  
    dimensions = (width, height)  
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90)
rotated1 = rotate(img, 180)
rotated2 = rotate(img, 360)
cv.imshow("rotated", rotated)
cv.imshow("rotated1", rotated1)
cv.imshow("rotated2", rotated2)

#Resizing
resized = cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
cv.imshow("resized image",resized)

#cropping
cropped = img[100:200, 200:500]
cv.imshow("cropped image", cropped)

#flipping an image
flipped = cv.flip(resized, -1) # 0 => x axis, 1=> y axis, -1 => both x and y flipp
cv.imshow("flipped image", flipped)
cv.waitKey(0)