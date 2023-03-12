import cv2 as cv
import numpy as np

def conv_transform(image):
    image_copy = image.copy()

    #for i in range(image.shape[0]):
    for i in range(len(image)):
        for j in range(len(image[1])):
            image_copy[i][j] = image[image.shape[0]-i-1][image.shape[1]-j-1]
    return image_copy        

def convolution(img, kernel):#image should be gray scale to avoid 3 color channels
    kernel = conv_transform(kernel)
    image_h = img.shape[0]
    image_w = img.shape[1]

    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]

    h = kernel_h//2
    w = kernel_w//2
    image_conv = np.zeros(img.shape)

    for i in range(h, image_h-h):
        for j in range(w, image_w-w):
            sum = 0

            for k in range(kernel_h):
                for l in range(kernel_w):
                    sum = sum + kernel[k][l]*img[i-h+k][j-w+l]
            image_conv[i][j] = sum
    cv.imshow("convolved image", image_conv)    
    return image_conv    

img  = cv.imread("chamanthi.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("conv_transform",conv_transform(gray))

kernel = [[1, 0, -1],[1, 0, -1],[1, 0, -1]] #vertical edge filter
convolution(gray, kernel)
