

#为什么是150，根据边缘检测函数返回值矩阵二值图得到
def  is_bound(value):
    if(value>150):
        return True
    else:
        return False