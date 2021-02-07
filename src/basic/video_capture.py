import cv2


def read_video_webcam():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(1, 100)
    while True:
        success, img = cap.read()
        cv2.imshow("video", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


path_test = r"C:\Users\Matheus\Desktop\opencv\data\videos\messi.mp4"
read_video(path_test)
read_video_webcam()
