import numpy as np
import cv2

pic= np.zeros((500, 500, 3), dtype='uint8')# creating a multi-dimensional numpy array

font= cv2.FONT_HERSHEY_DUPLEX

cv2.rectangle(pic, (0,0), (500,150), (123, 200, 98), 3, lineType= 8, shift=0)
cv2.line(pic, (0,0), (500,150), (123, 200, 98))
cv2.circle(pic, (250,250), 50, (255, 0, 255))  # 50 is the radius
cv2.putText(pic, 'Udemy', (100,100), font, 4, (123, 200, 98), 4, cv2.LINE_8)

cv2.imshow('Dark', pic)
cv2.waitKey(0)      #allows the image to be open for a while
cv2.destroyAllWindows()     