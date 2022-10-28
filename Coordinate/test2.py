# 开发时间 2022/10/25 13:01
# 开发时间 2022/10/24 15:39
# 开发时间 2022/7/13 15:58
# read the image
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt


np.set_printoptions(threshold=np.inf)
# 导入图像以及背景
# filename = "d/a"+str(i+1)+".jpg"
img_path = "../Img/baminton.jpg"
img = cv2.imread(img_path)
# bg = cv2.imread('930.png')
# 对比度调节
img = cv2.convertScaleAbs(img,0,3)
# 图像二值化
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 图像灰度化
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# 设置卷积核
kernel = np.ones((10, 10), np.uint8)
# 图像开运算,形态学开运算
result = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
# 高斯滤波降噪
lenna = cv2.GaussianBlur(result, (5, 5), 0)
# Canny边缘检测
canny = cv2.Canny(lenna, 0, 255)
# 显示边缘
# canny = cv2.resize(canny,(800,812))
cv2.imshow("demo", canny)
cv2.waitKey(0)