import cv2
import numpy as np
# from src.code.functions import rescale_frame

path = r"C:\Users\Matheus\Desktop\opencv\data\images\pez.jpg"
image = cv2.imread(path)
# image = rescale_frame(image, scale=0.5)
cv2.imshow("image", image)
print(image.shape)
blank = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("blank", blank)

# mascara
mask = cv2.circle(blank, (image.shape[1]//2, image.shape[0]//2), 100, 255, -1)
cv2.imshow("mask", mask)
# masked image
masked = cv2.bitwise_and(image, mask)
cv2.imshow("masked", masked)

cv2.waitKey(0)
