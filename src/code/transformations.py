import cv2
from src.code.functions import translate, rotate

path = r"C:\Users\Matheus\Desktop\opencv\data\images\ruta.jpg"
image = cv2.imread(path)

translated = translate(image, 100, 100)
rotated = rotate(image, 45)
flip = cv2.flip(image, 1)
cv2.imshow("flip", flip)
# cv2.imshow("trasladada", translated)
# cv2.imshow("rotated", rotated)
cv2.waitKey(0)
