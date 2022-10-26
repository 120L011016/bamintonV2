import edge_detection
import A_B_coordinate
def C_D(img_path):
    gray = edge_detection.detection(img_path)
    shape = gray.shape
    A,B=A_B_coordinate.A_B(img_path)
    right_ordinate = A[1]
    k=0
    i0 = 0
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            value = gray[i, j]
            if (value < 150):
                if(abs(j-right_ordinate)<50):
                    i0 = i
                    k=k+1
                    # j0=j
                    break


        if(k==10):
            break

    C = [i0,A[1]]
    D = [i0,B[1]]
    return C,D

