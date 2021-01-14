from math import sqrt
num=int(input("enter num to check:"))

prime=True
for i in range(2,int(sqrt(num)+1)):
    if num%i==0:
        prime=False
if prime:
    print("value you entered is prime")
else:
    print("not prime") 
