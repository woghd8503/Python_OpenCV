import cv2

src = cv2.imread("../img/swan.jpg")

_, binary = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)

cv2.namedWindow("binary")
cv2.resizeWindow("binary", 640, 480)
cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()