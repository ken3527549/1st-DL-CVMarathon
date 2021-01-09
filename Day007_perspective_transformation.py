import cv2
import time
import os
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(path + '/lena.png')

img_perspective = img.copy()
h, w = img.shape[:2]

# 設定四對點，並取得 perspective 矩陣
point1 = np.array([[60, 40], [420, 40], [420, 510], [60, 510]], dtype=np.float32)
point2 = np.array([[0, 80], [w, 120], [w, 430], [0, 470]], dtype=np.float32)
M = cv2.getPerspectiveTransform(point1, point2)

# perspective 轉換
img_perspective = cv2.warpPerspective(img, M, (w, h))

# 組合 + 顯示圖片
img_show = np.hstack((img, img_perspective))
while True:
    cv2.imshow('perspective transform', img_show)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break