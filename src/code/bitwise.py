import cv2
import numpy as np
from src.code.functions import rescale_frame

path = r"C:\Users\Matheus\Desktop\opencv\data\images\pez.jpg"
image = cv2.imread(path)
image = rescale_frame(image, scale=1)
print(image.shape)
blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv2.imshow("rectangle", rectangle)
circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)
cv2.imshow("circle", circle)
# bitwise operaciones
# interseccion de regiones
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow("bitwise_and", bitwise_and)
# suma de regiones
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow("bitwise_or", bitwise_or)
# non insterseciones entre dos images
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("bitwise_xor", bitwise_xor)
# invierte el color binario de la imagen que se le pasa
bitwise_not = cv2.bitwise_not(rectangle)
cv2.imshow("bitwise_not", bitwise_not)

cv2.waitKey(0)
