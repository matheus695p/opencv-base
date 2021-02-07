import cv2

path = r"C:\Users\Matheus\Desktop\opencv\data\images\2.jpg"
image = cv2.imread(path)
print("high", image.shape[0])
print("width", image.shape[1])
print("BGR", image.shape[2])
# resize de una imagen
image_resize = cv2.resize(image, (300, 300))
# image croped
image_cropped = image[0:200, 200:500]

# plot image
cv2.imshow("image", image)
cv2.imshow("image resize", image_resize)
cv2.imshow("image cropped", image_cropped)

cv2.waitKey(0)
