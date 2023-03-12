import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow("Blank", blank)

#1.paint the image a certain color
blank[200:300, 300:400] = 0,255,255
cv.imshow("yellow", blank)

#2.draw a rectangle
# cv.rectangle(blank,(0,0),(255, 255), (255, 0, 0), thickness = 2)
# cv.rectangle(blank,(0,0),(255, 255), (255, 0, 0), thickness = cv.FILLED)
# cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness = cv.FILLED)
# cv.rectangle(blank,(0,0),(255, 255), (255, 0, 0), thickness = -1)
# cv.imshow("blank draws", blank)

#3.Draw a circle
# cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255), thickness=-1)
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255), thickness=-1)
cv.imshow("circle on blank",blank)

#4.Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness = 3)
cv.line(blank, (300,110),(450, 500) , (255, 255, 255), thickness = 3)

cv.imshow("line", blank)

#5. write text on the image
cv.putText(blank, "hello, i am vineetha", (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 3)
cv.imshow("text on blank", blank)


# img = cv.imread("flower3.jpg")
# cv.imshow("flower", img)

cv.waitKey(0)