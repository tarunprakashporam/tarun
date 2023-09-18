import cv2
import numpy as np

# Load the pre-trained SSD model for face detection
net = cv2.dnn.readNetFromCaffe('path/to/deploy.prototxt', 'path/to/res10_300x300_ssd_iter_140000.caffemodel')

# Load an image from file
image = cv2.imread('image.jpg')

# Convert the image to grayscale for face detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with detected faces
cv2.imshow('Face Detection', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
