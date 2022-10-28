from CoordinateV2 import edge_detection ,Top_bottom_coordinate,is_bound

#轮廓最左边的点，左右边的点，在保证球头竖直情况下可以得到球头的宽度，不能确定最左边的点具体是A还是C，同理右边
def left_right(img_path):


    top,bottom = Top_bottom_coordinate.Top_bottom_coordinate(img_path)
    gray = edge_detection.detection(img_path)
    shape = gray.shape

    top_x = top[0]
    top_y = top[1]

    left = [top_x, top_y]
    right = [top_x, top_y]

    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            value = gray[i, j]
            if (is_bound(value)):
                if (left[1] > j):
                    left[1] = j
                    left[0] = i
                if (right[1] < j):
                    right[1] = j
                    right[0] = i

    return left, right

