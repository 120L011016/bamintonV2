import edge_detection
import cv2
import A_B_coordinate
import C_D_coordinate
import top_bottom_line
import Top_coordinate
# jj=edge_detection.detection("../Img/baminton.jpg")
#
#
# cv2.imshow("demo",jj)
# cv2.waitKey(0)
img_path = "../Img/baminton.jpg"
A,B=A_B_coordinate.A_B(img_path)
C,D=C_D_coordinate.C_D(img_path)
top,bottom,middle = top_bottom_line.top_bottom(img_path)
T = Top_coordinate.Top_coordinate(img_path)
print(A+B)


