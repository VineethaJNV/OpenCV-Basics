import numpy as np
import cv2

# Load image and convert to grayscale
image = cv2.imread("Metro_Images_Edge_Detection27-02-23\cropped\crop_0_People_Behind_glass_partition.jpg")
cv2.imshow("image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours of edges
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through contours and remove vertical lines using tangent function
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w > h:
        for i in range(w):
            theta = np.arctan(h/w)
            j = int(y + i*np.tan(theta))
            image[j][x+i] = [0, 0, 0]

# Save result
cv2.imwrite('result.jpg', image)
