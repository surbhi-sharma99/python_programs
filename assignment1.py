# assignment 1:-
"""num = int(input("enter a number:"))

if num%5==0 and num%7!=0:
     print("number is only divisible by 5")
else:
    print("either number is divisible by 7 or by both 7 & 5")"""
# solution 2:-

num =int(input("enter a number here:"))

if num%5==0:
     if num%7!=0:
         print("number is divisible by 5 but not dividible by 7")
     else:
         print("number is divisible by 5 and 7")
else:
    print("number is not divisible by 5 or 7")
