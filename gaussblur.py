import cv2
import numpy as np

pic= cv2.imread('Royswag.jpg', 0)   #0--greyscale, 1---white

matrix= (7,7)

blur= cv2.GaussianBlur(pic, matrix, 0)      # The sigma parameter is set at zero so that it does not 
# affect the gaussian Blur function

cv2.imshow('blurred', blur)
cv2.waitKey(0)      #allows the image to be open for a while
cv2.destroyAllWindows() 

