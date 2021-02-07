import cv2
import numpy as np
import matplotlib.pyplot as plt
from src.code.functions import rescale_frame

path = r"C:\Users\Matheus\Desktop\opencv\data\images\pez.jpg"
image = cv2.imread(path)
image = rescale_frame(image, scale=0.7)
print(image.shape)
blank = np.zeros(image.shape[:2], dtype="uint8")
# gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# mask
mask = cv2.circle(blank, (image.shape[1]//2 - 100, image.shape[0]//2 - 50),
                  100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)

# histograma de la imagen en grus
gray_hist = cv2.calcHist([gray], [0], mask, [256], [0, 256])

# colores a verificar
colors = ("b", "g", "r")

plt.figure()
plt.title("color histograms")
plt.xlabel("bins")
plt.ylabel("# de pixeles")

for i, col in enumerate(colors):
    print(i, col)
    hist = cv2.calcHist([image], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.xlim([0, 256])
plt.show()


plt.figure()
plt.title("Gray scale histogram")
plt.xlabel("bins")
plt.ylabel("# de pixeles")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()


cv2.imshow("image", image)
cv2.imshow("gray", gray)
cv2.imshow("mask", masked)
cv2.waitKey(0)
