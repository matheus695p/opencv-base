import cv2
import numpy as np


image = np.zeros((512, 512, 3), np.uint8)
text = "OPENCV"

# image[:] = 255, 0, 0
cv2.line(image, (0, 0), (image.shape[1], image.shape[0]), (255, 0, 9), 3)
cv2.rectangle(image, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.circle(image, (200, 200), 50, (0, 255, 0), 5)
cv2.putText(image, text, (300, 200),
            cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 150, 0), 3)

cv2.imshow("image", image)
cv2.waitKey(0)
