import edge_detection


# 计算顶部和底部的行
def top_bottom(img_path):
    gray = edge_detection.detection(img_path)
    shape = gray.shape
    top = 200
    temp = 999
    tempj = 0
    arri = []
    for i in range(0, shape[0], 10):
        for j in range(0, shape[1]):
            value = gray[i, j]
            # print("",value)
            if (value < 150):
                print('行:', i, '列:', j, "", '像素值', value)
                if (j < temp):
                    detaj = temp - j
                    dvalue = detaj - tempj
                    print('差值:', dvalue)
                    tempj = detaj
                    print('列的偏移量:', detaj)
                    if (abs(dvalue) < 10):
                        print('差值较低的行数', i)
                        arri.append(i)
                temp = j
                if (i < top):
                    top = i
                bottom = i
    middle = int((bottom - top) / 2)
    return top,bottom,middle