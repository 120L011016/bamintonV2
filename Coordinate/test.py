import numpy as np

import right_x
import Top_coordinate
import TopV2
import A_B_C_D
import cv2
img_path = "../Img/baminton.jpg"
# left,right=right_x.right_x(img_path)
# Top = Top_coordinate.Top_coordinate(img_path)
Top2 = TopV2.Top(img_path)
A,B,C,D = A_B_C_D.A_B_C_D(img_path)
h =1

# 创建黑色图像
img = np.zeros((930,930, 3), np.uint8)

# 绘制直线
cv2.line(img,(A[1],A[0]),(B[1],B[0]), (55, 255, 155), 5)
cv2.line(img,(D[1],D[0]),(B[1],B[0]), (55, 255, 155), 5)
cv2.line(img,(A[1],A[0]),(C[1],C[0]), (55, 255, 155), 5)
cv2.ellipse(img,(Top2[1],C[0]),(Top2[1]-C[1],Top2[1]-C[1]),0,180,360,(55, 255, 155), 5)
# 显示图像
cv2.imshow("line", img)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
