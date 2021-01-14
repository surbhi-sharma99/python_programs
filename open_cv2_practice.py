import cv2
import numpy as np
from time import sleep
from random import randint

image = np.zeros((400,400,3), dtype=np.uint8)
#x=0

#cv2.imshow("window_name_anything",image)
while True:
    image[:,:]=[randint(0,255),randint(0,255),randint(0,255)]
    #image[200:220,x:x+20]=[20,67,89]
    #image[x:x+20,200:220]=[120,67,89]

    cv2.imshow("window_name_anything",image)
    if cv2.waitKey(10) == ord("q"):
        break
    #x+=1
    #if x == 380:
        #x=0
cv2.destroyAllWindows()    
