import numpy as np
import cv2

# Create a blank image
img = np.zeros([512, 512, 3], np.uint8)

# Draw a line
cv2.line(img, (50, 50), (450, 450), (147, 96, 44), 5)

# Draw a rectangle
cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 255), 3)

# Draw an ellipse
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 255, 255), -1)

# Draw a circle
cv2.circle(img, (400, 100), 50, (0, 255, 0), -1)

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
