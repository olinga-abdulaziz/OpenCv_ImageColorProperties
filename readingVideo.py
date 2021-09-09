import cv2

cap=cv2.VideoCapture("res/vid.mp4")

while True:
    succes,img=cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

