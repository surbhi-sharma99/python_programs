fibonacci=[1,1]

second_last=1

last=1

for i in range(25):
    new=last+second_last
    
    fibonacci.append(new)
    
    last,second_last=new,last
    
for j in fibonacci:
    print(j)
    
