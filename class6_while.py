"""
from time import sleep
i=1
while True:
    print("*"*i)
    sleep(.3)
    i=i+1
"""
'''
from time import sleep
while True:
    for i in range(1,8):
        print("*"*i)
        sleep(.3)
    for j in range(6,0,-1):
        print("*"*j)
        sleep(.3)
    
'''
"""
from time import sleep

i=1
c=1
while True:
    print("*"*i)
    sleep(.3)
    i=i+c

    #decrease at one point
    if i==7:
        c=-1
    if i==1:
        c=1
"""
"""
from time import sleep

i=1
c=1
while True:
    print("*"*i)
    #sleep(.3)
    i=i+c

    #decrease at one point
    if i==7 or i==1:
        c=0-c
"""

from time import sleep

i=1
c=1
size=7
while True:
    print("*"*i)
    sleep(.3)
    i=i+c

    #decrease at one point
    if (i==size) or (i==1):
        c=0-c
        if i==1:
            size=size+7
