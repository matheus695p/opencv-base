import cv2
import numpy as np
import matplotlib.pyplot as plt
from src.code.functions import rescale_frame

path = r"C:\Users\Matheus\Desktop\opencv\data\images\lambo.jpg"
image = cv2.imread(path)
image = rescale_frame(image, scale=0.5)
# blank image
blank = np.zeros(image.shape, dtype="uint8")
# gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# hsv color
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# lab
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
# corrected image
corrected = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow("image", image)
cv2.imshow("image gray", gray)
cv2.imshow("image hsv", hsv)
cv2.imshow("image LAB", lab)
cv2.waitKey(0)

plt.imshow(corrected)
plt.show()
