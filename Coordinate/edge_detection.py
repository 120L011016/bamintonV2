import cv2
import numpy as np
# np.set_printoptions(threshold=np.inf)
#输入一张图，输入改图的边缘检测图
def detection(img_path):


    #图片路径
    bg_path = "../Img/background.png"
    # 导入图像以及背景
    img = cv2.imread(img_path)
    bg = cv2.imread(bg_path)

    # 图像二值化
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 图像灰度化
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # 设置卷积核
    kernel = np.ones((3, 3), np.uint8)
    # kernel = np.ones((10, 10), np.uint8)
    # 图像开运算,形态学开运算
    result = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    # 高斯滤波降噪
    lenna = cv2.GaussianBlur(result, (5, 5), 0)
    # Canny边缘检测，50为低阈值low，150为高阈值high
    canny = cv2.Canny(lenna, 0, 255)


    # 轮廓提取
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 根据二值图找轮廓
    # 将轮廓绘制在背景上
    cv2.drawContours(bg, contours, 0, (0, 0, 255), 3)  # 把轮廓画在原图上（0,0,255） 表示 RGB 三通道，红色
    # 图像二值化
    bg = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)
    # 图像灰度化
    gray = cv2.cvtColor(bg, cv2.COLOR_RGB2GRAY)

    return gray