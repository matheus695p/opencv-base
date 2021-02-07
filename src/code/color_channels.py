import cv2
import numpy as np
from src.code.functions import rescale_frame

path = r"C:\Users\Matheus\Desktop\opencv\data\images\lambo.jpg"
image = cv2.imread(path)
image = rescale_frame(image, scale=0.5)
# blank images
blank = np.zeros(image.shape[:2], dtype="uint8")
# separación de los colores
b, g, r = cv2.split(image)
# merge channels
merged = cv2.merge([b, g, r])

blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

cv2.imshow("b", blue)
cv2.imshow("g", green)
cv2.imshow("r", red)
cv2.imshow("image", image)
cv2.waitKey(0)
