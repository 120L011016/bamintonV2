import cv2
import numpy as np


def cal_area(img_path):
    '''
    计算图像边框面积
    :param img_path: 待计算图像路径
    :return: 边缘面积大小
    '''
    img = cv2.imread(img_path)
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
    # Canny边缘检测，50为低阈值low，150为高阈值high
    canny = cv2.Canny(lenna, 50, 150)
    # 轮廓提取
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 根据二值图找轮廓
    area = 0
    for i in contours:
        area += cv2.contourArea(i)

    return area


def cal_abs(path1, path2):
    '''
    计算两张图像边缘面积差的绝对值
    :param path1: 图像1
    :param path2: 图像2
    :return: 绝对值
    '''
    area1 = cal_area(path1)
    area2 = cal_area(path2)
    return abs(area1-area2)

#
# cal_area('../1_camB.jpg')