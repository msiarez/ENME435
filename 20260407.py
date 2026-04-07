import numpy as np
imoport matplotlib.pyplot as plt
import cv2
import imutils

camera = cv2.imread("testimage_Spring2026.jpg")
cv2.imshow("Original Frame", camera)

camera_copy = cv2.imread("testimage_Spring2026.jpg")
box = cv2.rectangle(Camera_copy, (0, 260), (640, 400), (0, 255, 0))
cv2.imshow("Box Coordinates", box)

#Define points array for transformation
pts1 = np.float32([[0, 260], [640, 260], [0, 400], [640, 400]])
pts2 = np.float32([[0, 0], [480, 0], [0, 640], [480, 640]])

#Apply Perspective Transform Algorithm
matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(camera, matrix, (500,600))

#Transformed Capture
cv2.imshow('frame1', result)

cv2.waitKey(0)
