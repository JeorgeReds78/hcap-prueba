import cv2

img = cv2.imread('imagen.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(img.shape)
print(img[0][0])

cv2.imshow('image', img)
cv2.waitKey(0)

