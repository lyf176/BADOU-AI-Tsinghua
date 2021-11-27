import cv2
import numpy as np

def function(img):
    height,weight,channel = img.shape
    Empty_Img = np.zeros((960,540,channel),np.uint8)
    sh = 960/height
    sw = 540/weight

    for i in range(960):
        for j in range(540):
            x = int(i/sh)
            y = int(j/sw)

            Empty_Img[i,j] = img[x,y]

    return Empty_Img

shuru = cv2.imread('mx.jpg')
zoom = function(shuru)
print(zoom)
print(zoom.shape)
cv2.imshow("nearest interp",zoom)
cv2.waitKey(0)
