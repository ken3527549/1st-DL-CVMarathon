import cv2
import time
import os
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(path + '/lena.png')


# 矩形
img_rect = img.copy()
cv2.rectangle(img_rect, (60, 40), (420, 510), (0, 0, 255), 3)

while True:
    cv2.imshow('image', img_rect)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

# 線
img_line = img.copy()
cv2.line(img_line, (60, 40), (420, 510), (0, 0, 255), 3)

while True:
    cv2.imshow('image', img_line)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break


# 文字
img_text = img.copy()
cv2.putText(img_text, '(60, 40)', (60, 40), 0, 1, (0, 0, 255), 2)

while True:
    cv2.imshow('image', img_text)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break


img_hw = img.copy()
point1 = (60, 40)
point2 = (420, 510)

"""
對明亮度做直方圖均衡
"""
# 原始 BGR 圖片轉 HSV 圖片
img_hw = cv2.cvtColor(img_hw, cv2.COLOR_BGR2HSV)

# 對明亮度做直方圖均衡 -> 對 HSV 的 V 做直方圖均衡
img_hw[..., -1] = cv2.equalizeHist(img_hw[..., -1])

# 將圖片轉回 BGR
img_hw = cv2.cvtColor(img_hw, cv2.COLOR_HSV2BGR)

"""
畫出人物矩形邊框
"""
cv2.rectangle(img_hw, point1, point2, (0, 0, 255), 3)

"""
水平鏡像 + 縮放處理 (0.5 倍)
"""
# 水平鏡像 (圖片)
img_hw = img_hw[:, ::-1, :]

# 縮放處理
img_hw = cv2.resize(img_hw, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

while True:
    cv2.imshow('image', img_hw)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
