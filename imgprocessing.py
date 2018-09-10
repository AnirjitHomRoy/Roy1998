import numpy as np
import cv2

pic= np.zeros((500, 500, 3), dtype='uint8')# creating a multi-dimensional numpy array
# fill this array with the required data to form an image
# The 3 dimensional array creates a channel of RGB
cv2.rectangle(pic, (0,0), (500,150), (123, 200, 98), 3, lineType= 8, shift=0)
#3 denotes the base colours we have, the 3 coordinates constitute the colour of the rectangle's border
#linetype- dotted or straight, shift- 
cv2.imshow('Dark', pic)
cv2.waitKey(0)      #allows the image to be open for a while
cv2.destroyAllWindows()     