num=int(input("enter numbers"))
arr=[]
arr.append(num)         
max_sum=0
min_sum=0
for i in arr:
    if i<arr[4]:
        min_sum=min_sum+arr[i]
for i in arr:
    if i==arr[0]:
        max_sum=0
    else:
        max_sum=max_sum+i
print(min_sum,max_sum)        
