#even odd-
"""
li=[87,6,8,749,365,873,458,73,5,23,69,82,6,3,58,764,38,7,5]
even=[]
odd=[]
for i in li:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even is:-")
for j in even:
    print(j)
print("_"*30)
print("odd is:-")
for k in odd:
    print(k)
"""    
#count
li=["Tyrion lannister","jon targaryen","daenerys targaryen","brian of tarth","queen lagertha","ragnar lothbrok"]
count=0
count1=0

for i in li:
    
    count=count+i.count("a")
    count1=count1+i.count("e")
print("number of a is "+str(count))
print("number of e is "+str(count1))
    
    
