import cv2
from src.code.functions import rescale_frame

path = r"C:\Users\Matheus\Desktop\opencv\data\images\pez.jpg"
image = cv2.imread(path)
image = rescale_frame(image, scale=0.5)

# gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# simple theresholding
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# inverse
threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
# adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)


cv2.imshow("image", image)
cv2.imshow("gray", gray)
cv2.imshow("simple thresh", thresh)
cv2.imshow("inverse thresh", thresh_inv)
cv2.imshow("adaptive thresh", adaptive_thresh)

cv2.waitKey(0)
