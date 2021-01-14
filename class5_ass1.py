a =int(input("Enter a: "))
b=int(input("enter b: "))
hcf=1
if a<b:
    small=a
else:
    small=b
for i in range(2,small+1):
    if (a%i==0) and (b%i==0):
        hcf=i
        break
print("hcf: "+str(hcf))        
