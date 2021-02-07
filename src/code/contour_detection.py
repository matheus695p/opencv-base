import cv2
import numpy as np
from src.code.functions import rescale_frame

path = r"C:\Users\Matheus\Desktop\opencv\data\images\lambo.jpg"
image = cv2.imread(path)
image = rescale_frame(image, scale=0.5)
# blank image
blank = np.zeros(image.shape, dtype="uint8")
# imagen en gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur de image
blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
# detector de bordes
canny = cv2.Canny(blur, 125, 175)

ret, thresh = cv2.threshold(gray, 125, 175, cv2.THRESH_BINARY)

# find contours methods
contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST,
                                         cv2.CHAIN_APPROX_SIMPLE)
print("Número de contornos", len(contours))

cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)

cv2.imshow("gato", image)
cv2.imshow("gato", gray)
cv2.imshow("gato", blur)
cv2.imshow("canny", canny)
cv2.imshow("thresh", thresh)
cv2.imshow("blank", blank)


cv2.waitKey(0)
