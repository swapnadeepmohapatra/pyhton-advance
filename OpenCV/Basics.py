import cv2

img = cv2.imread('C:\\Users\\Home PC\\Desktop\\cert_img\\lco_python.jpg', 1)
cv2.imshow('IMG', img)
cv2.waitKey()
cv2.destroyAllWindows()

print(img.shape)
