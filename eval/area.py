from Coordinate import edge_detection
#衡量面积的程序，未完成
def area(standard_path,img_path):
    gray = edge_detection.detection(img_path)
    shape = gray.shape

    gray1 = edge_detection.detection(standard_path)
    shape1 = gray1.shape

    area = 8
    area1 = 9

    return abs(area-area1)


