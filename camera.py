import win32api
import winGuiAuto
import win32gui
import win32con
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    scale_percent = 30
    wi = int(frame.shape[1] * scale_percent / 100)
    he = int(frame.shape[0] * scale_percent / 100)
    frame = cv.resize(frame, (wi, he))
    # frame = cv.flip(frame, 0)
    # write the flipped frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
cv.destroyAllWindows()