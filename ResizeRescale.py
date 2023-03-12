import cv2 as cv

#reading images
image = cv.imread("flower3.jpg")
cv.imshow("flower", image)

def changeRes(width, height):
    #live video
    vid.set(3, width)
    vid.set(4, height)

def rescaleFrame(frame, scale = 0.2):
    #images, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(image)
cv.imshow("resized image",resized_image)

# reading videos
# vid = cv.VideoCapture(0)
vid = cv.VideoCapture("FlowerVideo.mp4")
print(type(vid))

while True:
    isTrue, frame = vid.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow("video frame", frame)
    cv.imshow("resized frame", frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
vid.relase()
cv.destroyAllWindows()

cv.waitKey(0)