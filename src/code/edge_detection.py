import cv2
import numpy as np
from src.code.functions import rescale_frame

path = r"C:\Users\Matheus\Desktop\opencv\data\images\lambo.jpg"
image = cv2.imread(path)
image = rescale_frame(image, scale=0.5)

# gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# laplacian
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
# sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
combine = cv2.bitwise_or(sobelx, sobely)
# canny edge detector
canny = cv2.Canny(gray, 150, 175, None)

# cv2.imshow("image", image)
# cv2.imshow("gray", gray)
cv2.imshow("laplacian", lap)
cv2.imshow("sobel", combine)
cv2.imshow("canny", canny)
cv2.waitKey(0)
