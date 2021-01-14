
import cv2
import numpy as np
from time import sleep
from random import randint

image = np.zeros((400,400,3), dtype=np.uint8)

while True:
    image[:,:]=[randint(0,255),randint(0,255),randint(0,255)]
    

    cv2.imshow("window_name_anything",image)
    if cv2.waitKey(10) == ord("q"):
        break
    
cv2.destroyAllWindows()
