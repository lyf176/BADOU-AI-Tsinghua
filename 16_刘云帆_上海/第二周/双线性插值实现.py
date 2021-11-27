import numpy as np
import cv2

def bilinear_interpolation(img,out_dim):

#1,  原图长宽     目的图长宽
    src_h,src_w,channel = img.shape
    dst_h,dst_w = out_dim[0],out_dim[1]
    print("src_h, src_w = ", src_h, src_w)
    print("dst_h, dst_w = ", dst_h, dst_w)

#2,  生成一张和目的图片大小一样的空白图片
    dst_img = np.zeros((dst_h,dst_w,3),dtype=np.uint8)

#3， 原图和目的图片长宽的概率
    scale_x,scale_y = float(src_w) / dst_w, float(src_h) / dst_h

#4, 一个个的打印出每个通道的每个坐标： (dst_x,dst_y)
    for i in range(3):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):

#5, 求原图的坐标（x0,y0）,(x,y),(x1,y1)
                #求（x,y）
                src_x,src_y = (dst_x+0.5)*scale_x-0.5,(dst_y+0.5)*scale_y-0.5
                #求（x0,y0）
                src_x0,src_y0 = int(np.floor(src_x)),int(np.floor(src_y))
                #求（x1,y1）
                src_x1,src_y1 = min(src_x0+1,src_w-1),min(src_y0+1,src_h-1)

#6, 求f(r1),f(r2)即temp0，temp1.   然后求f（x，y）即 dst_img[dst_y,dst_x,i]

                temp0 = (src_x1 - src_x) * img[src_y0,src_x0,i] + (src_x - src_x0) * img[src_y0,src_x1,i]
                temp1 = (src_x1 - src_x) * img[src_y1,src_x0,i] + (src_x - src_x0) * img[src_y1,src_x1,i]
                dst_img[dst_y,dst_x,i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)

    return dst_img

if __name__ == '__main__':
    img = cv2.imread('xx.jpg')
    dst = bilinear_interpolation(img,(1200,540))
    cv2.imshow('bilinear interp',dst)
    cv2.waitKey()



