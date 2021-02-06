import cv2

path = r"C:\Users\Matheus\Desktop\opencv\data\images\cards.jpg"
image = cv2.imread(path)
print("high", image.shape[0])
print("width", image.shape[1])
print("BGR", image.shape[2])

cv2.imshow("image", image)
cv2.waitKey(0)
