import cv2
import os
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))
gray_img = cv2.imread(path + '/len_full.jpg',cv2.IMREAD_GRAYSCALE)
rgb_img =  cv2.imread(path + '/len_full.jpg')

img_gray = cv2.imread(path + '/len_full.jpg', cv2.IMREAD_GRAYSCALE)
img_bgr = cv2.imread(path + '/len_full.jpg')
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_hls = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)
img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)

# change color space
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_hls = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)
img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)

# change saturation
def change_hsv_saturation(img_hsv, change_percentage):
    # 操作飽和度時候需要轉成百分比(原本是0~255)
    img_hsv = img_hsv.astype('float32')
    # 轉成小數點並調降兩成飽和度
    img_hsv[...,1] = img_hsv[...,1]/255 + change_percentage
    # 判斷所有值介於0~1之間
    img_hsv[img_hsv[...,1] < 0] = 0
    img_hsv[...,1] = img_hsv[...,1] * 255
    img_hsv = img_hsv.astype('uint8')
    return cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

img_hsv_down = change_hsv_saturation(img_hsv, -0.2)
img_hsv_up = change_hsv_saturation(img_hsv, 0.2)
img_hsv_combined = np.hstack((img_bgr, img_hsv_down, img_hsv_up))

# Histogram Equalization
def one_channel_equalizeHist(img):
    return cv2.equalizeHist(img)

# gray Histogram Equalization
img_gray_eqHist = one_channel_equalizeHist(img_gray)
img_gray_equalHist_combined = np.hstack((img_gray, img_gray_eqHist))

# GBR Histogram Equalization directly
img_bgr_eqHist = img_bgr
img_bgr_eqHist[...,0] = one_channel_equalizeHist(img_bgr[...,0])
img_bgr_eqHist[...,1] = one_channel_equalizeHist(img_bgr[...,1])
img_bgr_eqHist[...,2] = one_channel_equalizeHist(img_bgr[...,2])
img_bgr_combined = np.hstack((img_bgr, img_bgr_eqHist))

# convert RGB to HSV then Histogram Equalization
img_hsv_eqHist = img_hsv
img_hsv_eqHist[...,-1] = one_channel_equalizeHist(img_hsv_eqHist[...,-1])
_img_bgr = cv2.cvtColor(img_hsv_eqHist, cv2.COLOR_HSV2BGR)
img_hsv_combined_eqHist = np.hstack((img_bgr, _img_bgr))



# 調整對比/明亮度
# alpha: 控制對比度 (1.0~3.0)
# beta: 控制明亮度 (0~255)
img = img_bgr
add_contrast = cv2.convertScaleAbs(img, alpha=2.5, beta=0)
add_lighness = cv2.convertScaleAbs(img, alpha=1.0, beta=50)
# 組合圖片 + 顯示圖片
img_contrast_light = np.hstack((img, add_contrast, add_lighness))

# cv2.imshow('img_gray', img_gray)
# cv2.imshow('img_bgr', img_bgr)
# cv2.imshow('img_hsv', img_hsv)
# cv2.imshow('img_hls', img_hls)
# cv2.imshow('img_lab', img_lab)
# cv2.imshow('img_hsv_down', img_hsv_down)
# cv2.imshow('img_hsv_up', img_hsv_up)
# cv2.imshow('img_gray', img_gray)
cv2.imshow('change saturation by changing the color space', img_hsv_combined)
cv2.imshow('gray equal histogram', img_gray_equalHist_combined)
cv2.imshow('RGB histogram equalization directly', img_bgr_combined)
cv2.imshow('hsv histogram equalization', img_hsv_combined_eqHist)
cv2.imshow('adjust contrast and brighness', img_contrast_light)

cv2.waitKey(0)
cv2.destroyAllWindows()
