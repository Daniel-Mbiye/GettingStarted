import cv2

print("Hello world!")
print(cv2.__version__)

img = cv2.imread("lena.png")

cv2.imshow("Output", img)
cv2.waitKey(0)
