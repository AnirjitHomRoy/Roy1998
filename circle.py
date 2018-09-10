import numpy as np
import cv2


pic= np.zeros((500, 500, 3), dtype='uint8')# creating a multi-dimensional numpy array
# fill this array with the required data to form an image
# The 3 dimensional array creates a channel of RGBcv2.line(pic, (120,540), (350,350), (123, 200, 38))
color= (255, 0, 255)
cv2.circle(pic, (250,250), 50, color)  # 50 is the radius
cv2.imshow('Dark', pic)
cv2.waitKey(0)      #allows the image to be open for a while
cv2.destroyAllWindows()     