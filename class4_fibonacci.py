second_last=1

last=1

print(second_last,last)
for i in range(25):
    new=last+second_last
    print(new)
    last,second_last=new,last
    
