import cv2
import numpy as np

pic= cv2.imread('Royswag.jpg')
cols= pic.shape[1]      #finding the dimensions of the image
rows= pic.shape[0]      #finding the dimensions of the image

M= np.float32([[1,0,150],[0,1,70]])    #creating the translation matrix
#150 along the x-axis and 70 along the y-axis
#x-axis-----positive is as usual to the right
#y-axis-----positive is toward the bottom 

shifted= cv2.warpAffine(pic, M, (cols, rows))
cv2.imshow('shifted', shifted)

cv2.waitKey(0)      #allows the image to be open for a while
cv2.destroyAllWindows() 
