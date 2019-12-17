import cv2
import time
import os, glob

cap = cv2.VideoCapture(0)
cnt = 0

print("runnning")
while True:
    try:
        filepath = "./static/img/img{}.jpg".format(cnt)
        ret, frame = cap.read()
        cv2.imwrite(filepath, frame)
        time.sleep(5)
        cnt += 1
        if not cnt%10:
            [os.remove(file) for file in glob.glob("./static/img/*.jpg")]
    except KeyboardInterrupt:
        break

cap.release()

