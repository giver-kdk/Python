import cv2
import numpy as np

img = cv2.imread('giver.jpg')
img = cv2.resize(img,(500,500))
cv2.imshow('before',img)

image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh,bimage1) = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

(thresh,bimage2) = cv2.threshold(image,150,255,cv2.THRESH_BINARY)

#both_image = np.hstack([image,bimage1.bimahe2])

cv2.imshow('Black_and_white_after_first_threshold',bimage1)
cv2.waitKey(0)
cv2.imshow('Black_and_white_after_second_threshold_value',bimage2)
cv2.waitKey(0)
cv2.destroyAllWindows()