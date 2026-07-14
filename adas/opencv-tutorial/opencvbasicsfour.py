import numpy as np
import cv2
cap = cv2.VideoCapture('/Users/swaroopmahendrashinde/Downloads/NEW FOLDER FOR PHOTOS/16 Pro/IMG_7659.mov')
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width, height),(255,255,255),5)
    img = cv2.line(img, (0,height), (width, 0),(255,255,255),5)
    img = cv2.rectangle(img, (500,500), (900,900), (255,128,65), 5)
    img = cv2.circle(img, (1000,1000), 120, (0,0,255), 10)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Swaroop', (200,height-100),font, 5, (0,0,0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
