
#灰度化和二值化实现
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
import cv2

#灰度化实现

# 1、cv2.imread:将图片转换为三维数字矩阵-赋予给变量picture
picture = cv2.imread("mx.jpg")

# 2、获取图片长和宽的像素个数有多少个 长：h   宽：w
h,w = picture.shape[:2]

# 3、创建一张和当前图片大小一样的单通道图片
picture_gray = np.zeros([h,w],picture.dtype)
c,k = picture_gray.shape[:2]

# h=1920  w=1080
for i in range(h):
    for j in range(w):
        p = picture[i,j]
        picture_gray[i,j] =int(p[0]*0.11 + p[1]*0.59 +p[2]*0.3)

print(picture_gray)
print("image show gray: %s"%picture_gray)
cv2.imshow("image show gray", picture_gray)


plt.subplot(131)
picture = plt.imread("mx.jpg")
plt.imshow(picture)
print("---picture mx---")
print(picture)

#灰度化

plt.subplot(132)
plt.imshow(picture_gray,cmap='gray')
print("---picture gray---")
print(picture_gray)

#二值化
r,w = picture_gray.shape
for i in range(r):
    for j in range(w):
        if picture_gray[i,j] <= 128:
            picture_gray[i,j] = 0
        else:
            picture_gray[i,j] = 1


plt.subplot(133)
plt.imshow(picture_gray,cmap='gray')
print("---picture binary---")
print(picture_gray)




plt.show()

