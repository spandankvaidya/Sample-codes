import numpy as np
import cv2
cap = cv2.VideoCapture('C:\\Users\\Spandan Vaidya\\Desktop\\test.mp4')
i=0
while cap.isOpened():
    while(i%4==0):
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
