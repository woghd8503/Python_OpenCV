import numpy as np
import cv2

src = cv2.imread('../img/psycho_but_ok.jpg', cv2.IMREAD_COLOR)

x, y = 50, 50

add_dst = cv2.add(src, 100)
sub_dst = cv2.subtract(src, 100)

cv2.imshow('src', src)
cv2.imshow('add_dst', add_dst)
cv2.imshow('sub_dst', sub_dst)

cv2.waitKey()
cv2.destroyAllWindows()