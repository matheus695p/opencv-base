# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:20:54 2021

@author: Matheus
"""
import cv2
from src.code.functions import rescale_frame

path = r"C:\Users\Matheus\Desktop\opencv\data\videos\messi.mp4"
cap = cv2.VideoCapture(path)

while True:
    success, img = cap.read()
    resize_img = rescale_frame(img, scale=0.2)
    cv2.imshow("video resized", resize_img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
