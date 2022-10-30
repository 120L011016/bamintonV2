import math

import cv2
import numpy as np
import re
import os
from PIL import Image

#边缘检测函数，返回一个二值图
def detection(img_path):

    # #生成宽1080，长1920的白色背景
    # bg = np.zeros((1080, 1920), np.uint8)
    # # 白色背景
    # bg.fill(255)

    np.set_printoptions(threshold=np.inf)
    # # 导入图像
    img = cv2.imread(img_path)
    #下采样
    # img = cv2.pyrDown(cv2.imread(img_path, cv2.IMREAD_UNCHANGED))
    # 对比度调节
    img = cv2.convertScaleAbs(img, 0, 3)
    # 图像二值化
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 图像灰度化
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # 设置卷积核
    kernel = np.ones((10, 10), np.uint8)
    # kernel = np.ones((10, 10), np.uint8)
    # 图像开运算,形态学开运算
    result = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    # 高斯滤波降噪
    lenna = cv2.GaussianBlur(result, (5, 5), 0)
    # Canny边缘检测，50为低阈值low，150为高阈值high
    canny = cv2.Canny(lenna, 0, 255)


    # # 轮廓提取
    # contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 根据二值图找轮廓
    # # 将轮廓绘制在背景上
    # cv2.drawContours(bg, contours, 0, (0, 0, 255), 3)  # 把轮廓画在原图上（0,0,255） 表示 RGB 三通道，红色
    # # 图像二值化
    # bg = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)
    # # 图像灰度化
    # gray = cv2.cvtColor(bg, cv2.COLOR_RGB2GRAY)

    return canny
def opration_on_detection(img_path):
    canny = detection(img_path)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    #找出contours中最大的一组，之给最大的一组数据做下列操作
    max_score = 0
    max_contour = 0
    for j in contours:
        if (j.size > max_score):
            max_score = j.size
            max_contour = j
    c = max_contour


    #找最小矩形，默认图没有旋转
    x, y, w, h = cv2.boundingRect(c)
    top_y = y
    left_upper = [x,y]
    #绘制矩阵
    # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


    # 查找最小区域，适用于图旋转后
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

    #椭圆拟合
    test = c
    new_c = []
    # middle = abs((box[0][1]+box[1][1])/2)
    middle = abs(top_y+h/2)
    shape = test.shape
    for i in range(0, shape[0]):
        k = test[i]
        if(k[0][1]<middle):
            new_c.append(k)
    new_c = np.array(new_c)

    (x, y), radius = cv2.minEnclosingCircle(new_c)
    # 转换为整数
    center = (int(x), int(y))
    radius = int(radius)
    # 画圆
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)

    (cx, cy), (a, b), angle = cv2.fitEllipse(new_c)
    #center 为焦点距离的一半
    center_t = math.sqrt(b*b-a*a)
    #e为离心率
    e = center_t/a
    # 绘制椭圆
    cv2.ellipse(img, (np.int32(cx), np.int32(cy)),
               (np.int32(a / 2), np.int32(b / 2)), angle, 0, 360, (0, 0, 255), 2, 8, 0)

    #绘制边界
    # cv2.drawContours(img, contours, -1, (255, 0, 0), 3)
    cv2.drawContours(img, contours, -1, (0, 0, 255), -1)

    #得到的绘制后的图像，得到的矩阵左上角的点，高度。宽度，得到的离心率
    return img,left_upper,w,h,e,a,b,w*h/2+math.pi*radius*radius/2
def  area(img_path):

    #必须要闭合的才能做

    # canny = detection(img_path)
    # contous, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    # max_score = 0
    # max_number = 0
    # for j in contous:
    #     if (j.size > max_score):
    #         max_score = j.size
    #         max_number = j
    # m = max_number
    #
    # c = m
    #
    # # 定义能包含此裂缝的最小矩形，矩形为水平方向
    # left_x = min(c[:, 0, 0])
    # right_x = max(c[:, 0, 0])
    # down_y = max(c[:, 0, 1])
    # up_y = min(c[:, 0, 1])
    #
    # # 构造包含轮廓的矩形的所有像素点
    # Nx = 2 ** 8
    # Ny = 2 ** 8
    # pixel_X = np.linspace(left_x, right_x, Nx)
    # pixel_Y = np.linspace(up_y, down_y, Ny)
    # # 从坐标向量中生成网格点坐标矩阵
    # xx, yy = np.meshgrid(pixel_X, pixel_Y)
    # # 筛选出轮廓内所有像素点
    # in_list = []
    # for i in range(pixel_X.shape[0]):
    #     for j in range(pixel_X.shape[0]):
    #         # cv2.pointPolygonTest可查找图像中的点与轮廓之间的最短距离.当点在轮廓外时返回负值，当点在内部时返回正值，如果点在轮廓上则返回零
    #         # 统计裂缝内的所有点的坐标
    #         if cv2.pointPolygonTest(c, (xx[i][j], yy[i][j]), False) > 0:
    #             in_list.append((xx[i][j], yy[i][j]))
    # in_point = np.array(in_list)
    # # # 绘制轮廓
    # # img_original = cv2.imread(img_path)
    # # cv2.drawContours(img_original, contous, -1, (0, 0, 255), -1)
    # # cv2.imshow('Inscribed_circle', img_original)
    # # # cv2.imwrite('inference/output/Inscribed_circle.png', img_original)
    # # cv2.waitKey(0)
    # return in_point.shape[0]


    #对于不闭合的也能计算
    img = cv2.pyrDown(cv2.imread(img_path, cv2.IMREAD_UNCHANGED))
    ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area = 0
    for i in contours:
        area += cv2.contourArea(i)

    # cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
    # cv2.imshow("contours", img)

    cv2.waitKey(1)
    return area

def cal_abs(path1, path2):
    '''
    计算两张图像边缘面积差的绝对值
    :param path1: 图像1
    :param path2: 图像2
    :return: 绝对值
    '''
    area1 = area(path1)
    area2 = area(path2)
    return abs(area1-area2)

def eval_all(img_path):


    #默认摆正
    # rotate(img_path)
    stand_area_score = 0
    stand_circularity_score = 0
    stand_height_score = 0


    aggregate = opration_on_detection(img_path)
    # 归一化，需要做
    area_score = area(img_path)
    circularity_score = aggregate[4]
    height_score = aggregate[3]

    stand_area_score = aggregate[7]
    stand_circularity_score = 0
    stand_height_score = 600

    area_Dif = abs(stand_area_score-area_score)
    circularity_Dif = abs(stand_circularity_score-circularity_score)
    height_Dif = abs(stand_height_score - height_score)

    area_threshold = 250000
    circularity_threshold = 0.35
    height_threshold = 100

    cv2.imshow(img_path, aggregate[0])

    # cv2.waitKey(1000)
    # cv2.destroyWindow(img_path)

    cv2.waitKey(0)
    # 主要的逻辑检测部分
    if((area_Dif>area_threshold)or(circularity_Dif>circularity_threshold)or(height_Dif>height_threshold)):
        return False
    else:
        return True


    #展示效果部分
    # print(img_path+"    :  area_score:  "+str(area_score)+"   ,circularity_score:   "+str(circularity_score)+"   ,height_score:   "+str(height_score))
    # print(img_path+"    :  area_Dif:  "+str(area_Dif)+"   ,circularity_Dif:   "+str(circularity_Dif))
    #
    # print(img_path+"  a = "+str(aggregate[5])+"         b = "+str(aggregate[6]))
    #
    # cv2.imshow(img_path, aggregate[0])
    #
    # cv2.waitKey(1000)
    # cv2.destroyWindow(img_path)

    # cv2.waitKey(0)

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

def Batch_processing(Img_Dir):

    image_list = os.listdir(Img_Dir)

    #按照开头的数字进行排序
    strsort(image_list)


    for image in image_list:
        img_path = Img_Dir+'/'+image

        result = eval_all(img_path)
        print(img_path+"的结果："+str(result))
        #         核心代码，把对每一张图片要做的事情放在这里
        #         评估所有的照片质量




# img_path = "../Img/baminton_1.jpg"
# area = area(img_path)
# print(area)
#Img_Dir 为图片路径
Img_Dir = "../Batch_Img"
Batch_processing(Img_Dir)
