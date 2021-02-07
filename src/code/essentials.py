import cv2
import numpy as np

path = r"C:\Users\Matheus\Desktop\opencv\data\images\ruta.jpg"
image = cv2.imread(path)
# kernel of image
kernel = np.ones((5, 5), np.uint8)

# imagen en blanco y negro
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur filter
image_blur = cv2.GaussianBlur(image_gray, (7, 7), 0)
# edge detector
image_canny = cv2.Canny(image, 400, 400)
# image dialation
image_dialation = cv2.dilate(image_canny, kernel, iterations=1)
# erosion of a image
image_erosion = cv2.erode(image_dialation, kernel, iterations=1)


cv2.imshow("gray image", image_gray)
cv2.imshow("blur image", image_blur)
cv2.imshow("canny", image_canny)
cv2.imshow("dialation image", image_dialation)
cv2.imshow("erosion image", image_erosion)
cv2.waitKey(0)
