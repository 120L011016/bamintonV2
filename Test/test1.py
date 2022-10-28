from CoordinateV2 import edge_detection
import re
import os
import cv2

import cv2
import numpy as np

def sort_key(s):
    # 排序关键字匹配
    # 匹配开头数字序号
    if s:
        try:
            c = re.findall('^\d+', s)[0]
        except:
            c = -1
        return int(c)

def strsort(alist):
    alist.sort(key=sort_key)
    return alist
Img_Dir = "../Batch_Img"

image_list = os.listdir(Img_Dir)
strsort(image_list)
for image in image_list:
    img = "../Batch_Img/"+image

    img = cv2.pyrDown(cv2.imread(img, cv2.IMREAD_UNCHANGED))
    img = cv2.imread(image)
    ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 90, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    max_score = 0
    max_number = 0
    for j in contours:
        if(j.size>max_score):
            max_score = j.size
            max_number = j
    c = max_number

    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 查找最小区域
    rect = cv2.minAreaRect(c)
    # 计算最小面积矩形的坐标
    box = cv2.boxPoints(rect)
    # 将坐标标准化为整数
    box = np.int0(box)
    # 绘制等高线
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)
    # 计算最小封闭圆的中心和半径
    (x, y), radius = cv2.minEnclosingCircle(c)
    # 转换为整数
    center = (int(x), int(y))
    radius = int(radius)
    # 画圆
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)


    cv2.drawContours(img, c, -1, (255, 0, 0), 3)
    cv2.imshow("contours", img)
    cv2.waitKey(0)







    # cv2.imshow("demo", Draw.max_domin(img))
    # cv2.waitKey(0)