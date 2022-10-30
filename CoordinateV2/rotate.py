import os
import re

from PIL import Image
from CoordinateV2 import edge_detection
import numpy as np
import cv2
def rotate(img_path):

    canny = edge_detection.detection(img_path)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找出contours中最大的一组，之给最大的一组数据做下列操作
    max_score = 0
    max_contour = 0
    for j in contours:
        if (j.size > max_score):
            max_score = j.size
            max_contour = j
    c = max_contour

    # 找最小矩形，默认图没有旋转
    x, y, w, h = cv2.boundingRect(c)
    top_y = y
    left_upper = [x, y]
    # 绘制矩阵
    # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)



    # 椭圆拟合
    test = c
    new_c = []
    down_C = []
    # middle = abs((box[0][1]+box[1][1])/2)
    middle = abs(top_y + h / 2)
    shape = test.shape
    for i in range(0, shape[0]):
        k = test[i]
        if (k[0][1] < middle):
            new_c.append(k)
        else:
            down_C.append(k)
    new_c = np.array(new_c)
    down_C = np.array(down_C)


    (cx, cy), (a, b), angle = cv2.fitEllipse(new_c)
    cv2.ellipse(img, (np.int32(cx), np.int32(cy)),
                (np.int32(a / 2), np.int32(b / 2)), angle, 0, 360, (0, 0, 255), 2, 8, 0)
    print(angle)
    if(angle>10):
        angle = 0

    im = Image.open(img_path)

    im_rotate = im.rotate(-angle)


    im_rotate.save(img_path[:-3]+"_mify.jpg")


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

        rotate(img_path)
        #         核心代码，把对每一张图片要做的事情放在这里
        #         评估所有的照片质量
#TEST  --------------------------
# m = math.atan(0.48)
# k = math.degrees(m)
# img_path = "../Img/17_camB.jpg"
# rotate(img_path)
# print("ok")
Img_Dir = "../Img/Batch_goog"
Batch_processing(Img_Dir)