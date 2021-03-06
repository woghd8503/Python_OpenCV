import cv2


src = cv2.imread("../img/cameraman.jpg", cv2.IMREAD_GRAYSCALE)

# 자동으로 임계값을 찾아주는 알고리즘 적용(Otsu, Triangle)
# _, binary = cv2.threshold(src, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
_, binary = cv2.threshold(src, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

cv2.namedWindow("binary")
dst = cv2.resize(binary, dsize=(640, 480), interpolation=cv2.INTER_AREA)
cv2.imshow("binary", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()