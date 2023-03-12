import cv2 as cv
import pandas as pd
import numpy as np
#reading images
image = cv.imread("flowerHD.jpg")
print(type(image))
cv.imshow("flower Image", image)

#reading videos
# vid = cv.VideoCapture(0)
vid = cv.VideoCapture("FlowerVideo.mp4")
print(type(vid))

while True:
    isTrue, frame = vid.read()
    cv.imshow("video frame", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
vid.relase()
cv.destroyAllWindows()

cv.waitKey(0)