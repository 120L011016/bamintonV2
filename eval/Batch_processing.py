import eval_all
import os
import re
import area
from Coordinate import edge_detection
from Coordinate import Draw
import cv2
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

#评估所有的照片质量
def Batch_processing(Img_Dir):

    image_list = os.listdir(Img_Dir)

    #按照开头的数字进行排序
    strsort(image_list)

    #标准图片的路径
    standard_path = "../Img/baminton_1.jpg"
    for image in image_list:
        image_dir = Img_Dir+'/'+image


        #核心代码，把对每一张图片要做的事情放在这里
        #评估所有的照片质量
        score  = eval_all.eval_all(standard_path,image_dir)
        print(image+'+'+score)

# 计算图片的面积
def Batch_processing_show(Img_Dir):
    image_list = os.listdir(Img_Dir)

    # 按照开头的数字进行排序
    strsort(image_list)

    # 标准图片的路径
    standard_path = "../Img/baminton_1.jpg"
    for image in image_list:
        image_dir = Img_Dir + '/' + image

        # 核心代码，把对每一张图片要做的事情放在这里
        # 计算图片的面积
        score = area.cal_area(image_dir)
        print(image + '  :  ' + str(score))
        # gray = edge_detection.detection(image_dir)
        # cv2.imshow(image, gray)
        Draw.Draw(image)
        # cv2.waitKey(0)


    score = area.cal_area(standard_path)
    print(standard_path + '  :  ' + str(score))


#Test-----------------------------------------------------

Img_Dir = "../Batch_ok"
Batch_processing_show(Img_Dir)

