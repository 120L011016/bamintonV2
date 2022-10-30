from CoordinateV2 import edge_detection,is_bound


#计算返回顶点的坐标
def Top_bottom_coordinate(img_path):
    gray = edge_detection.detection(img_path)
    shape = gray.shape
    top = [shape[0],0]
    bottom = [0,0]

    for i in range(0, shape[0]):  # shape[0]X轴（从左到右）
        for j in range(0, shape[1]):
            # 获取像素点
            value = gray[i, j]  # 一幅图的所有像素点
            # print("",value)
            # 获取轮廓
            if (is_bound.is_bound(value)):  # 轮廓边的点
                if(i<top[0]):
                    top[0] = i
                    top[1] = j
                if (i > bottom[0]):
                    bottom[0] = i
                    bottom[1] = j


    return top,bottom










#Test--------------------------------------------
#
# img_path = "../Img/baminton_1.jpg"
# # Draw_stand_imitate(img_path)
# print(Top_bottom_coordinate(img_path))

