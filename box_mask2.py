import cv2 as cv
import numpy as np
#smoothing
roi = cv.imread('picture5.jpg')
roi_gray = cv.cvtColor(roi,cv.COLOR_BGR2GRAY)

mask = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])
output_box = np.zeros((roi.shape[0],roi.shape[1]),dtype=np.uint8)
#output_box = np.zeros((roi.shape[0],roi.shape[1])) # dtype기본값은 float

for j in range(1,roi.shape[0]-1):
    for i in range(1,roi.shape[1]-1):
        sum = 0
        for r in range(-1,2):
            for c in range(-1,2):
                sum += roi_gray.item(j+r,i+c)* mask.item(r+1,c+1)  #mask 값
        sum //= 9  # mask 요소값의 합
        output_box.itemset(j,i,sum)

cv.imshow('origin',roi_gray)
cv.imshow('box_mask',output_box)
cv.waitKey(0)
cv.destroyAllWindows()
#박스 마스크