import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)
# normal image
img=cv2.imread("res/pic.jpeg")
# gray image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# blur image
blur=cv2.GaussianBlur(gray,(7,7),0)
# showing edges on image
imgCanny=cv2.Canny(img,100,100)
# Dilating image
imgDilate=cv2.dilate(imgCanny,kernel,iterations=1)
# eroded image
imgErode=cv2.erode(imgDilate,kernel,iterations=1)
cv2.imshow("Normal Image",img)
cv2.imshow("Gray Image",gray)
cv2.imshow("BlurImage",blur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilation Image",imgDilate)
cv2.imshow("Eroded Image",imgErode)
cv2.waitKey(0)