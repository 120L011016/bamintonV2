import edge_detection
import Top_coordinate
#计算返回左下角和右下角两个点的坐标
def A_B(img_path):
    gray = edge_detection.detection(img_path)
    shape = gray.shape
    top,j0 = Top_coordinate.Top_coordinate(img_path)
    arr1 = []
    for i in range(top + 1, shape[0], 6):
        for j1 in range(0, j0 + 1):
            value = gray[i, j1]
            if (value < 150):
                p1 = [i, j1]
                print("p1", p1)

                for j2 in range(0, j0):
                    i2 = i + 2
                    value = gray[i2, j2]
                    if (value < 150):
                        p2 = [i2, j2]
                        print("p2", p2)

                        for j3 in range(0, j0):
                            i3 = i2 + 2
                            value = gray[i3, j3]
                            if (value < 150):
                                p3 = [i3, j3]
                                print("p3", p3)
                                xielv1 = abs((p1[0] - p2[0]) / (p1[1] - p2[1] + 1e-10))
                                xielv2 = abs((p2[0] - p3[0]) / (p2[1] - p3[1] + 1e-10))
                                if (xielv2 == xielv1):
                                    #                                print("A",p2)
                                    arr1.append(p3)
                                    print(arr1)
                                    i1 = i3 + 1
                                else:
                                    i1 = i3 + 1
                                break
                        break
                break

    #   j1=0
    A = []
    A = arr1[len(arr1) - 1]
    arr2 = []
    for i in range(top + 1, shape[0], 6):
        for j1 in range(j0 + 1, shape[1]):
            value = gray[i, j1]
            if (value < 150):
                p1 = [i, j1]
                print("p1", p1)

                for j2 in range(j0 + 1, shape[1]):
                    i2 = i + 2
                    value = gray[i2, j2]
                    if (value < 150):
                        p2 = [i2, j2]
                        print("p2", p2)

                        for j3 in range(j0 + 1, shape[1]):
                            i3 = i2 + 2
                            value = gray[i3, j3]
                            if (value < 150):
                                p3 = [i3, j3]
                                print("p3", p3)
                                xielv1 = abs((p1[0] - p2[0]) / (p1[1] - p2[1] + 1e-10))
                                xielv2 = abs((p2[0] - p3[0]) / (p2[1] - p3[1] + 1e-10))
                                if (xielv2 == xielv1):
                                    #                                print("A",p2)
                                    arr2.append(p3)
                                    print(arr2)
                                    i1 = i3 + 1
                                else:
                                    i1 = i3 + 1
                                break
                        break
                break

        j1 = j0 + 1
    B = []
    B = arr2[len(arr2) - 1]
    return A,B