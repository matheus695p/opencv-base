import cv2

base = r"C\Users\Matheus\Desktop\opencv\data\hardcascades"
path_classifier = base + "haarcascade_frontalface_efault.xml"
path = r"C:\Users\Matheus\Desktop\opencv\data\images\lena.jpg"


faceCascade = cv2.CascadeClassifier(path_classifier)
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
