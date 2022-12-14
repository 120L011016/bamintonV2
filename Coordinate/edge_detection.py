import cv2
import numpy as np

from PIL import Image
# np.set_printoptions(threshold=np.inf)
#输入一张图，输入改图的边缘检测图
#返回值必须是一个闭合的轮廓，且轮廓外的值均相等
#轮廓值为255，非轮廓值为0
def detection(img_path):

    #生成宽1080，长1920的白色背景
    bg = np.zeros((1080, 1920), np.uint8)
    # 白色背景
    bg.fill(255)

    np.set_printoptions(threshold=np.inf)
    # 导入图像
    img = cv2.imread(img_path)

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


    # 轮廓提取
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 根据二值图找轮廓
    # 将轮廓绘制在背景上
    cv2.drawContours(bg, contours, 0, (0, 0, 255), 3)  # 把轮廓画在原图上（0,0,255） 表示 RGB 三通道，红色
    # 图像二值化
    bg = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)
    # 图像灰度化
    gray = cv2.cvtColor(bg, cv2.COLOR_RGB2GRAY)

    return gray


#失败，不太可取
def detectionv2(img_path):
    img = Image.open(img_path)

    img_array = np.array(img)

    gray = img_array[:, :, 0]

    shape = gray.shape

    for i in range(0, shape[0]):  # shape[0]X轴（从左到右）
        for j in range(0, shape[1]):
            # 获取像素点
            value = gray[i, j]  # 一幅图的所有像素点
            # print("",value)
            # 获取轮廓
            if (value < 150):  # 轮廓边的点
                gray[i, j] = 0


    return gray

