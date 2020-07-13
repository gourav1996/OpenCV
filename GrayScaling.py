import cv2
image = cv2.imread('./images/input.jpg')

cv2.waitKey()

# Gray scale 
gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale', gray_scale)
cv2.waitKey()
cv2.destroyallwindows()
