import os
import cv2

camera = cv2.VideoCapture(0)



while True:
    ret, frame = camera.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cascade = cv2.CascadeClassifier('cascade/haarcascade_resistors_0.xml')

    found = cascade.detectMultiScale(frame_gray)

    amount_found = len(found)

    if amount_found != 0:
        for (x, y, width, height) in found:
            cv2.rectangle(frame, (x,y), (x + height, y + width), (0, 255, 0), 5)

    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
camera.release()
cv2.destroyAllWindows