from Coordinate import A_B_C_D
import Coordinate
from Coordinate import TopV2
#衡量高度的程序
def height(standard_path,img_path):
    A,B,C,D = A_B_C_D.A_B_C_D(standard_path)
    Top = TopV2.Top(standard_path)
    height_standard = A[0]-Top[0]

    A1, B1, C1, D1 = A_B_C_D.A_B_C_D(img_path)
    Top1 = TopV2.Top(img_path)
    height_standard1 = A1[0] - Top1[0]

    return abs(height_standard1-height_standard)