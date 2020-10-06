import cv2
import numpy as np

frame = cv2.imread('/home/gourav/Pictures/t2.png')
frame = cv2.resize(frame,(1280,720))

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,40,40])
upper_red = np.array([80,220,200])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame,frame, mask= mask)
median_blur = cv2.medianBlur(res, 15)

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    #cv2.drawContours(frame2, contour, -1, (0, 255, 0), 3)
    if cv2.contourArea(contour) > 2000:
        x,y,w,h = cv2.boundingRect(contour)
        frame2 = cv2.rectangle(median_blur,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow('frame',frame)
# cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('median_blur',median_blur)

cv2.waitKey(0   )


cv2.destroyAllWindows()
