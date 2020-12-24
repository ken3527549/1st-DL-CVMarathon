import cv2
import os
print(os.path.dirname(os.path.abspath(__file__)))
path = os.path.dirname(os.path.abspath(__file__))
gray_img = cv2.imread(path + '/len_full.jpg',cv2.IMREAD_GRAYSCALE)
rgb_img =  cv2.imread(path + '/len_full.jpg')
cv2.imshow('gray_image', gray_img)
cv2.imshow('rgb_image', rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
