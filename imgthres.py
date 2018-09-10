import cv2
import numpy as np

pic= cv2.imread('Royswag.jpg', 0)   #0--greyscale, 1---white
threshold_value= 100    # pixel value below which a pixel will get converted to black

(T_value, binary_threshold)= cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY)

''''(T_value, binary_threshold)= cv2.threshold(pic, threshold_value, 255, cv2.INVERSE_BINARY)
Inverse_binary will do the reverse---below the threshold it will give white''''

cv2.imshow('Binary', binary_threshold)

cv2.waitKey(0)      #allows the image to be open for a while
cv2.destroyAllWindows()     