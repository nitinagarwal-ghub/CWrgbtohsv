#pixel grayscale
"""
import cv2 

image = cv2.imread('pika.png')
cv2.imshow('Original Image',image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
cv2.imshow('grayscale image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('pika.png')
(row,col) = img.shape[0:2]

for i in range(row):
    for j in range(col):
        img[i,j] = sum(img[i,j]) * 0.33

cv2.imshow('Grayscale image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-----------------------------------------
#rotating image

import cv2

img = cv2.imread('pika.png')
(rows,cols) = img.shape[:2]

M = cv2.getRotationMatrix2D((cols / 2, rows/2),45,1)
res = cv2.warpAffine(img,M,(cols,rows))

cv2.imwrite('resultofrot.jpg', res)
resu_img = cv2.imread('resultofrot.jpg')
cv2.imshow('Rotation',resu_img)
cv2.waitKey(0)
cv2.destroyAllWindows

#------------------------------------------
#edge detection

img = cv2.imread('pika.png')
edges = cv2.Canny(img,100,200)

cv2.imwrite('resultofedgedet.jpg',edges)
res_img = cv2.imread('resultofedgedet.jpg')
cv2.imshow('Edge detection',res_img)
cv2.waitKey(0)
cv2.destroyAllWindows
"""
#convert from rgb to hsv
#hsv = hue saturation value

import cv2

image = cv2.imread('/Users/nasa/downloads/folder/OpenCv/pika.png')
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('RGB', image)
cv2.waitKey(0)
cv2.imshow('HSV', hsvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()