import cv2
import numpy as np

pic= cv2.imread('Royswag.jpg')
cols= pic.shape[1]      #finding the dimensions of the image
rows= pic.shape[0]      #finding the dimensions of the image

center= (cols/2,rows/2)
angle =90    # anticlockwise

M= cv2.getRotationMatrix2D(center, angle, 1)
# part of the image to be rotated, the angle, the scale

rotated= cv2.warpAffine(pic, M, (cols, rows))
cv2.imshow('rotated', rotated)


cv2.waitKey(0)      #allows the image to be open for a while
cv2.destroyAllWindows()     