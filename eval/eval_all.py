import area
import Circularity
import height

def eval_all(standard_path,img_path):
    proportion_area = 0.5
    proportion_height = 0.2
    proportion_Circularity = 0.3

    #归一化，需要做
    area_score = area.cal_abs(standard_path,img_path)
    Circularity_score = Circularity.Ciecularity(standard_path,img_path)
    height_score = height.height(standard_path,img_path)

    score = area_score*proportion_area + Circularity_score*proportion_Circularity + height_score * proportion_height

    if(score < 0.1):
        return 1
    else:
        return score