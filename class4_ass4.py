
r="11223, 12445, 11334, 12456, 11322, 13567, 11564, 12789"   
count=0
num=0
for i in range (0,54,7):
    if r[i:i+2]=="11":
        count+=1
    
print(str(count)+" start from 11")
for i in range (0,54,7):
     if int(r[i:i+5])%2:
        num+=1
print(str(num)+ " is odd")
