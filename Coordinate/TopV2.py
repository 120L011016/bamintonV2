from Coordinate import right_x

from CoordinateV2 import edge_detection


#TopV2 和 Top_Coordinate 都是求 顶点坐标的，不同的是，TopV2比Top_Coordinate要准
#TopV2 调用了函数求最左边最右边点的函数right_x
def Top(img_path):
    gray = edge_detection.detection(img_path)
    shape = gray.shape
    right,left=right_x.right_x(img_path)
    top_j=round((right[1]+left[1])/2)
    top_i = 0
    for i in range(0, shape[0]):
        value = gray[i, top_j]
        if (value > 150):
            top_i = i
            break
    return top_i,top_j
