from CoordinateV2 import edge_detection, Top_bottom_coordinate


#求最左边最右边点的函数right_x，调用了Top_coordinate
def right_x(img_path):
    top_x, top_y = Top_coordinate.Top_coordinate(img_path)
    gray = edge_detection.detection(img_path)
    shape = gray.shape

    left = [top_x, top_y]
    right = [top_x, top_y]
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            value = gray[i, j]
            if (value > 150):
                if (left[1] > j):
                    left[1] = j
                    left[0] = i
                if (right[1] < j):
                    right[1] = j
                    right[0] = i

    return left, right
