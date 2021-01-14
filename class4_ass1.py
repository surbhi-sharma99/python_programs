print("please enter your marks in between 0-100")

count=0
count1=0
total_marks=0

for i in range(1,6):
    
    marks=int(input("enter your "+ str(i) +" marks here:"))
    total_marks=total_marks+marks

    if marks<33:
        count+=1
    else:
        count1+=1

print("total marks: "+ str(total_marks))

print("number of fail student is: "+ str(count))

print("number of pass student is: "+str(count1))
