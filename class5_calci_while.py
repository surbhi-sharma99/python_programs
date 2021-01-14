print("calculator app: ")
while True:
    a= input("enter 1 num: ")
    
    if a=="exit":
        break
    elif a=="again":
        continue
    else:
        a=int(a)    
        
    b=input("enter 2 num: ")
    
    if b=="exit":
        break
    elif b=="again":
        continue
    else:
        b=int(b)
        
    o=input("enter operation you want to perform")
    
    if o=="exit":
        break
    elif o=="again":
        continue
    elif o=="+":
        result=a+b
        print("result is: "+ str(result))
