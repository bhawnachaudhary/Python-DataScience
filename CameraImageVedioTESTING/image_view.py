import cv2

im = cv2.imread('vedio testing/times_square.jpeg')
h,w,_ = im.shape
sm_img = cv2.resize(im,(w//2,h//2))

cv2.imshow("photo",im)

cv2.imshow("photo_small",sm_img)
print(im,type(im),im.shape)

cv2.waitKey(0)