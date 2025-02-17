
import cv2 as cv
from matplotlib import pyplot as plt

import copy


#python 图像翻转,自定义翻转
def fanzhuan(filename) :
    img = cv.imread(filename)

    size = img.shape
    iCopy = copy.deepcopy(img)
    iCopy1 = copy.deepcopy(img)
    iCopy2 = copy.deepcopy(img)
    h=size[0]
    w=size[1]
    for i in range(h):
      for j in range(w):
        iCopy[i,w-1-j] = img[i,j]#水平镜像
        iCopy1[h - 1 - i, j] = img[i, j]  # 垂直镜像
        iCopy2[h - 1 - i, w - 1 - j] = img[i, j]  # 对角镜像
    plt.subplot(221), plt.imshow(img)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(iCopy)
    plt.title('Remap shuiping Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(iCopy1)
    plt.title('Remap chuizhi Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(iCopy2)
    plt.title('Remap duijiao Image'), plt.xticks([]), plt.yticks([])
    plt.savefig("aaa.jpg")
    plt.show()
def fanzhuan2(filename) :
    img = cv.imread(filename)

    size = img.shape
    iCopy = copy.deepcopy(img)
    iCopy1 = copy.deepcopy(img)
    iCopy2 = copy.deepcopy(img)
    h=size[0]
    w=size[1]
    xImg = cv.flip(img, 1, dst=None)  # 水平镜像
    xImg1 = cv.flip(img, 0, dst=None)  # 垂直镜像
    xImg2 = cv.flip(img, -1, dst=None)  # 对角镜像
    plt.subplot(221), plt.imshow(img)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(xImg)
    plt.title('Remap shuiping Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(xImg1)
    plt.title('Remap chuizhi Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(xImg2)
    plt.title('Remap duijiao Image'), plt.xticks([]), plt.yticks([])
    plt.savefig("aaa.png")
    plt.show()





if __name__=='__main__':
    fanzhuan('aa.png')







