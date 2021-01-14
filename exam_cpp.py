"""
D={}
D[(1,2)]=3
D[3]=1,2
print(list(D.keys()))
"""
"""
print(bin(10))
"""
"""
a = "[1,2,3]"
b = "[4,5,6]"
print(a+b)
"""
"""
print("".join("hello world".split()))

"""
"""
D = {1:"a"}
D[0]="a"
D[1]="b"
print(D)
"""

"""
def fun(n):
    print(n*2)
if __name__=="__main__":
    fun("2")
"""
"""
a= list(range(1,4))
b=[1,2,3,4,5,6][3:]
print(a+b)
"""
"""
print("+".join(list("12345")))
"""
"""
try:
    a = 2+"2"
    print("wrong")
except:
    print("correct")
"""
"""

def fun(num):
for i in range(num):
yield i
return None
if __name__=="__main__":
print(list(fun(3)))
"""
"""
print("helloWORLD"[2::2])
"""
D  = {2:[1,2],}
D[[1,2]]=2
print(D)
