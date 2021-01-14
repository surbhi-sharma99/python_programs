students={}
name=""
marks=[]
while True:
    name=input("enter your name")
    if name=="exit":
        break
    for i in range(3):
        marks.append(int(input("enter your marks:")))
    students[name]=marks
    print(students)    
        
