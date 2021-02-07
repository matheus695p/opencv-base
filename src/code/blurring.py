import cv2
import numpy as np
from src.code.functions import rescale_frame

path = r"C:\Users\Matheus\Desktop\opencv\data\images\carretera.jpg"
image = cv2.imread(path)
image = rescale_frame(image, scale=0.5)
# blank images
blank = np.zeros(image.shape[:2], dtype="uint8")
kernel = (3, 3)
# averiging
average = cv2.blur(image, kernel)
# gaussian blur
gauss = cv2.GaussianBlur(image, kernel, 0)
# median blur
median = cv2.medianBlur(image, 3)
# bilateral blurring
bilateral = cv2.bilateralFilter(image, 5, 15, 15)

cv2.imshow("image", image)
cv2.imshow("average image", average)
cv2.imshow("gaussian image", gauss)
cv2.imshow("median image", median)
cv2.imshow("bilateral image", bilateral)

cv2.waitKey(0)
