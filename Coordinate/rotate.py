import math
from PIL import Image
import cv2
import numpy as np
from Coordinate import right_x
from Coordinate import edge_detection
def rotate(img_path):

    gray = edge_detection.detection(img_path)

    left,right = right_x.right_x(img_path)

    slope = ((left[0]-right[0])/(left[1]-right[1]))

    print(slope)

    h = math.atan(slope)
    a = math.degrees(h)

    im = Image.open(img_path)

    im_rotate = im.rotate(a-25)

    im_rotate.save(img_path[:-3]+"_mify.jpg")


#TEST  --------------------------
m = math.atan(0.48)
k = math.degrees(m)
img_path = "../Img/baminton.jpg"
rotate(img_path)
print("ok")