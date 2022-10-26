import right_x
import edge_detection

def A_B_C_D(img_path):
    gray = edge_detection.detection(img_path)
    shape = gray.shape

    left, right = right_x.right_x(img_path)

    width = right[1]-left[1]

    xiao = min(left[0],right[0])
    da = max(left[0],right[0])
    A = [da,left[1]]
    B = [da,right[1]]
    C = [xiao,left[1]]
    D = [xiao,right[1]]
    return A,B,C,D