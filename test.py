import cv2
gray_img = cv2.imread('E:\cygwin\home\Ken-Destop\python\len_full.jpg',cv2.IMREAD_GRAYSCALE)
rgb_img =  cv2.imread('E:\cygwin\home\Ken-Destop\python\len_full.jpg')
cv2.imshow('gray_image', gray_img)
cv2.imshow('rgb_image', rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
