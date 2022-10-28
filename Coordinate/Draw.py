import numpy as np

from Coordinate import TopV2
from Coordinate import A_B_C_D
from CoordinateV2 import edge_detection
import cv2


#输入一张图 ，调用 求顶点和 A，B，C，D 点的函数，大致画出一个标准的和一个轮廓的图像
def Draw(img_path):

    Top2 = TopV2.Top(img_path)
    # Top2 = Top_coordinate.Top_coordinate(img_path)
    A, B, C, D = A_B_C_D.A_B_C_D(img_path)

    # 创建白色图像
    img = np.zeros((1080, 1920, 3), np.uint8)
    img.fill(255)

    # 绘制直线
    cv2.line(img, (A[1], A[0]), (B[1], B[0]), (55, 255, 155), 5)
    cv2.line(img, (D[1], D[0]), (B[1], B[0]), (55, 255, 155), 5)
    cv2.line(img, (A[1], A[0]), (C[1], C[0]), (55, 255, 155), 5)
    #绘制圆
    cv2.ellipse(img, (Top2[1], C[0]), (Top2[1] - C[1], Top2[1] - C[1]), 0, 180, 360, (55, 255, 155), 5)
    # 显示图像
    cv2.imshow(img_path, img)

    # 等待显示
    cv2.waitKey(0)


def Draw_stand_imitate(img_path):

    Top2 = TopV2.Top(img_path)
    # Top2 = Top_coordinate.Top_coordinate(img_path)
    A, B, C, D = A_B_C_D.A_B_C_D(img_path)

    # # 创建白色图像
    # img = np.zeros((1080, 1920, 3), np.uint8)
    # img.fill(255)
    img = edge_detection.detection(img_path)

    # 绘制直线
    cv2.line(img, (A[1], A[0]), (B[1], B[0]), (55, 255, 155), 1)
    cv2.line(img, (D[1], D[0]), (B[1], B[0]), (55, 255, 155), 1)
    cv2.line(img, (A[1], A[0]), (C[1], C[0]), (55, 255, 155), 1)
    #绘制圆
    cv2.ellipse(img, (Top2[1], C[0]), (Top2[1] - C[1], Top2[1] - C[1]), 0, 180, 360, (55, 255, 155), 1)

    # # 导入图像
    # img_i = cv2.imread(img_path)
    #
    # # 图像二值化
    # image = cv2.cvtColor(img_i, cv2.COLOR_BGR2RGB)
    # # 图像灰度化
    # gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # # 设置卷积核
    # kernel = np.ones((3, 3), np.uint8)
    # # kernel = np.ones((10, 10), np.uint8)
    # # 图像开运算,形态学开运算
    # result = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    # # 高斯滤波降噪
    # lenna = cv2.GaussianBlur(result, (5, 5), 0)
    # # Canny边缘检测，50为低阈值low，150为高阈值high
    # canny = cv2.Canny(lenna, 0, 255)
    #
    # # 轮廓提取
    # contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 根据二值图找轮廓
    # # 将轮廓绘制在背景上
    # cv2.drawContours(img, contours, 0, (0, 0, 255), 3)  # 把轮廓画在原图上（0,0,255） 表示 RGB 三通道，红色
    # # 图像二值化
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # # 图像灰度化
    # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 显示图像
    cv2.imshow(img_path, img)

    # 等待显示
    cv2.waitKey(0)
def  max_domin(img_path):
    mask_sel = edge_detection.detection(img_path)
    # find all cohntours
    contours, hierarchy = cv2.findContours(mask_sel, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    max = 0
    max_are = 0
    for j in range(len(contours)):
        area = cv2.contourArea(contours[j])
        if(area>max_are):
            max = j
            max_are = area


    mask = cv2.drawContours(mask_sel, contours[max], 0, 255, cv2.FILLED)
    # 显示图像
    cv2.imshow(img_path, mask)

    # 等待显示
    cv2.waitKey(0)


#Test        ----------------------------
def morphology(img_path):
    mask_sel = edge_detection.detection(img_path)
    # 显示图像
    cv2.imshow(img_path, mask_sel)

    # 等待显示
    cv2.waitKey(0)
    open = cv2.morphologyEx(mask_sel, cv2.MORPH_OPEN, (7, 7), iterations=100)

    # 显示图像
    cv2.imshow(img_path, mask_sel)

    # 等待显示
    cv2.waitKey(0)
img_path = "../Batch_ok/16_camC.jpg"
img_path = "../Img/baminton.jpg"
# Draw_stand_imitate(img_path)
max_domin(img_path)
# morphology(img_path)