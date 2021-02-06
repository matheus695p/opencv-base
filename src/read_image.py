import cv2


# leer una imagen
def read_image(path):
    image = cv2.imread(path)
    cv2.imshow("salida", image)
    cv2.waitKey(0)
    return image


path = r"C:\Users\Matheus\Desktop\opencv\data\images\1.jpg"
image = read_image(path)
