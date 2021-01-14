#with default argument
"""def solve(a,b,o="+"):
    if o=="+":
        c=a+b
    elif o=="-":
        c=a-b
    else:
        c="wrong"
    print(c)
solve(2,4,"-")    
 """
"""
def solve(a,b=5,o="+"): #default values ,should always be on right
    if o=="+":
        c=a+b
    elif o=="-":
        c=a-b
    else:
        c="wrong"
    
    return c
print(solve(2,4,"-"))
print(solve(3,6))

"""
"""
amount=0
def simple_interest(p,t=1,r=10):
    amount=(p*r*t)/100
    return amount
print(simple_interest(4,3))
print((simple_interest(5)))
"""
def solve(a,b=5,o="all"): #default values ,should always be on right
    if o=="+":
        sum=a+b
    elif o=="-":
        sub=a-b
    elif o=="all":
        sum=a+b
        sub=a-b
        c="wrong"
    
    return c
print(solve(2,4,"-"))
print(solve(3,6))
