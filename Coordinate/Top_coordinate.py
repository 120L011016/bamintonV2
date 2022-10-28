from Coordinate import edge_detection
#计算返回顶点的坐标
def Top_coordinate(img_path):
    gray = edge_detection.detection(img_path)
    shape = gray.shape
    top = 200
    sign = 0
    # 求最高顶点
    j0 = 0
    for i in range(0, shape[0]):  # shape[0]X轴（从左到右），切片，步长：10
        k = 0
        for j in range(0, shape[1]):
            # 获取像素点
            value = gray[i, j]  # 一幅图的所有像素点
            # print("",value)
            # 获取轮廓
            if (value > 150):  # 轮廓边的点
                if (sign == 0):
                    top = i
                    j0 = j
                    sign = 1
                k = k + 1
        if (k != 0):
            j0 = j0 + round(k / 2)
            break
    return top,j0
