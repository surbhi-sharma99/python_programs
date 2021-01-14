"""
import cv2

import numpy as np

image =np.zeros((400,400,3),dtype=np.uint8)

image[:,:] =[20, 30, 250]  #bgr format

cv2.imshow("box.jpg", image)

"""

"""
import cv2

from time import sleep

import numpy as np

from random import randint

image =np.zeros((400,400,3),dtype=np.uint8)

while True:
    image[:,:]=[randint(0,255),randint(0,255), randint(0,255)]
    
    cv2.imshow("window_name_anything", image)

    if cv2.waitKey(10)==ord("q"):  ##waitkey functin takes ascci value so we use "ord" here
        break
    
    sleep(.1)

cv2.destroyAllWindows()    
"""


import cv2

from time import sleep

import numpy as np

from random import randint

image =np.zeros((400,400,3),dtype=np.uint8)

image[:,:]=[0, 200, 200]

x = 0

c = 1

while True:
    image_copy = image.copy()

    image_copy[200:200, x:x+20]= [200 , 50 , 50]

    cv2.imshow("window_name_anything", image_copy)

    if cv2.waitKey(10)==ord("q"):
        break
    
    x = x+c

    if x == 380:
        c = 0 - c
    if x == 0:
        c = 0 - c

cv2.destroyAllWindows()        

  
