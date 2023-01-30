import os
import cv2
import time



execution_path = os.getcwd()
camera = cv2.VideoCapture(0)

while True:
    start_time = time.time()

    ret, frame = camera.read()

    fpsInfo = "FPS: " + str(1.0 / (time.time() - start_time))
    print(fpsInfo)

    cv2.putText(frame, fpsInfo, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        
    cv2.imshow('Video', frame)
        
    if cv2.waitKey(1) & 0xFF == ord('1'):
        break
camera.release()
cv2.destroyAllWindows()
    