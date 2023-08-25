import cv2
import numpy as np
import stack



img = cv2.imread("Resources/lena.png")

imgStack = stack.stackImages(0.5, ([img, img, img]))

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)
cv2.imshow("ImageStack", imgStack)

cv2.waitKey(0)
