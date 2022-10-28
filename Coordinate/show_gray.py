from CoordinateV2 import edge_detection
import re
import os
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
Img_Dir = "../Batch_Img"

image_list = os.listdir(Img_Dir)
strsort(image_list)
for image in image_list:
    img = "../Batch_Img/"+image
    print(img)
    gray = edge_detection.detection(img)


    cv2.imshow("img",cv2.imread(img))
    cv2.waitKey(0)
    cv2.imshow("demo", gray)
    cv2.waitKey(0)

    # cv2.imshow("demo", Draw.max_domin(img))
    # cv2.waitKey(0)