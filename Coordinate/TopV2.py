import right_x

import edge_detection
def Top(img_path):
    gray = edge_detection.detection(img_path)
    shape = gray.shape
    right,left=right_x.right_x(img_path)
    top_j=round((right[1]+left[1])/2)
    top_i = 0
    for i in range(0, shape[0]):
        value = gray[i, top_j]
        if (value < 150):
            top_i = i
            break
    return top_i,top_j
