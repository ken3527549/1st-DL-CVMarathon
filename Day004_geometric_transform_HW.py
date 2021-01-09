import cv2
import time
import os
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(path + '/lena.png')

# 垂直翻轉
img_vflip = img[::-1, :, :]

# 組合 + 顯示圖片
hflip = np.vstack((img, img_vflip))
while True:
    cv2.imshow('flip image', hflip)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

# 將圖片縮小成原本的 20%
img_test = cv2.resize(img, None, fx=0.2, fy=0.2)
# 將圖片放大為"小圖片"的 8 倍大 = 原圖的 1.6 倍大
fx, fy = 8, 8
# 鄰近差值 scale + 計算花費時間
start_time = time.time()
img_area_scale = cv2.resize(img_test, None, fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
print('INTER_NEAREST zoom cost {}'.format(time.time() - start_time))
# 組合 + 顯示圖片
orig_img = cv2.resize(img, img_area_scale.shape[:2])
img_zoom = np.hstack((orig_img, img_area_scale))
while True:
    cv2.imshow('zoom image', img_zoom)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

# 設定 translation transformation matrix
# x 平移 100 pixel; y 平移 50 pixel
M = np.array([[1, 0, 100],
              [0, 1, 50]], dtype=np.float32)
shift_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# 組合 + 顯示圖片
img_shift = np.hstack((img, shift_img))
while True:
    cv2.imshow('shift image', img_shift)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break