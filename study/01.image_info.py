import cv2

src = cv2.imread("../img/OpenCV_Logo.png", cv2.IMREAD_GRAYSCALE)

print(src.ndim, src.shape, src.dtype)

src1 = cv2.imread("../img/OpenCV_Logo.png", cv2.IMREAD_COLOR)

print(src.ndim, src.shape, src.dtype)


