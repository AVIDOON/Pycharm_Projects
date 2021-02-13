import numpy as np
import cv2 as cv

video = cv.VideoCapture(0)

while(True):
    ret, frame = video.read()
    cv.imshow('xxx',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
