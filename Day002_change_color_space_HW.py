import cv2
import os
path = os.path.dirname(os.path.abspath(__file__))
gray_img = cv2.imread(path + '/len_full.jpg',cv2.IMREAD_GRAYSCALE)
rgb_img =  cv2.imread(path + '/len_full.jpg')

img_gray = cv2.imread(path + '/len_full.jpg', cv2.IMREAD_GRAYSCALE)
img_bgr = cv2.imread(path + '/len_full.jpg')
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_hsl = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)
img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_bgr', img_bgr)
cv2.imshow('img_hsv', img_hsv)
cv2.imshow('img_hsl', img_hsl)
cv2.imshow('img_lab', img_lab)
cv2.waitKey(0)
cv2.destroyAllWindows()
