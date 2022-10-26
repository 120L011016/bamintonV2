import cv2 as cv
import numpy as np
import edge_detection
# 读取文件
img_path = "../Img/baminton.jpg"
# origin = cv.imread(img_path, 1)
# img = cv.imread(img_path, 0)
gray = edge_detection.detection(img_path)
cv.imwrite("back.jpg",gray)
img1_path = "back.jpg"
origin = cv.imread(img1_path, 1)
img = cv.imread(img1_path, 0)
# 霍夫圆检测
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 100, param1=50, param2=30, minRadius=0, maxRadius=100)

circles = np.uint16(np.around(circles))

# 将检测到的圆圈标上去
for i in circles[0, :]:  # 遍历矩阵每一行的数据
    cv.circle(origin, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv.circle(origin, (i[0], i[1]), 2, (0, 0, 255), 3)

# 显示图像
cv.imshow("image", origin)
cv.waitKey(0)
cv.destroyAllWindows()