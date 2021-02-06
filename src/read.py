import cv2
print(cv2.__version__)


image = cv2.imread(r"data|images|foto1.jpg")

cv2.imshow("salida", image)
cv2.waitKey(0)
