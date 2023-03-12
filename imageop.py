import cv2
import numpy as np
from PIL import Image, ImageChops
import math
from PIL import Image 
import imutils
from skimage.metrics import structural_similarity

orig_img = cv2.imread("taj-mahal-agra-india-TAJ0217-9eab8f20d11d4391901867ed1ce222b8.jpg")
comparing_img = cv2.imread("filteredTaj.jpg")
# orig_img = cv2.imread("LinkedinProfile.png")
# comparing_img = cv2.imread("2023-02-15-09-44-10-639.png")

if orig_img.shape == comparing_img.shape:
    dissimilarities = cv2.subtract(orig_img, comparing_img)
    b, g, r = cv2.split(dissimilarities)
    print(cv2.countNonZero(b))
    print(cv2.countNonZero(g))
    print(cv2.countNonZero(r))
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("Images are same to the level of pixel")
    else:
        print("Images are different but are of same size")
#elif orig_img.shape != comparing_img.shape:
#    dissimilarities = cv2.subtract(orig_img, comparing_img)

grey_scale1 = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
grey_scale2 = cv2.cvtColor(comparing_img, cv2.COLOR_BGR2GRAY)
difference = cv2.absdiff(grey_scale1, grey_scale2)
cv2.imshow("absolute difference is", difference )

(similar, diff) = structural_similarity(grey_scale1, grey_scale2, full = True)
diff = (diff*255).astype("uint8")
cv2.imshow("difference using structural_similarity", diff)

threshold = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cv2.imshow("threshold", threshold)

contour = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = imutils.grab_contours(contour)

# for c in contour:
#     if cv2.contourArea(c) > 100:
#         x,y,w,h = cv2.boundingRect(c)
#         cv2.rectangle(orig_img, (x,y), (x+w, y+h), (0,0,255), 2)
#         cv2.rectangle(comparing_img, (x,y), (x+w, y+h), (0,0,255), 2)
#         cv2.putText(comparing_img, "Similarity Percentage:"+str(similar),(10,30), cv2.FONT_HERSHEY_SIMPLEX, .7, (0,0,255), 2)

# x = np.zeros((360,10,3), np.uint8)
# result = np.hstack((orig_img, x, comparing_img))
# cv2.imshow("Differences", result)


# def root_mean_diff(img1, img2):
#     difference = ImageChops.difference(img1, img2)
#     hist = difference.histogram()
#     square = (j*((i%256)**2) for i, j in enumerate(hist))
#     sum = sum(square)
#     rms = math.sqrt(sum/float(img1.size[0] * img2.size[1]))
#     return rms

# result = root_mean_diff(orig_img, comparing_img)
# print(result)


orig_img = cv2.resize(orig_img,(1000, 600))
comparing_img = cv2.resize(comparing_img,(1000, 600))
dissimilarities = cv2.resize(dissimilarities, (1000,600))


cv2.imshow("orig_name", orig_img)
cv2.imshow("comparing_img", comparing_img)
cv2.imshow("Differences",dissimilarities)

cv2.waitKey(0)
cv2.destroyAllWindows()





