l=[]
for i in range(4):
    l1=[]
    name=input("enter your name:")
    l1.append(name)
    for j in range(3):
        marks=int(input("enter marks:"))
        l1.append(marks)

    l.append(l1)
print(l)
