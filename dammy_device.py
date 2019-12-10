import cv2
import time

cap = cv2.VideoCapture(0)
cnt = 0

while True:
    try:
        filepath = "./static/img/img{}.jpg".format(cnt)
        ret, frame = cap.read()
        cv2.imwrite(filepath, frame)
        time.sleep(5)
        cnt += 1
    except KeyboardInterrupt:
        break

cap.release()

