#assignment 2:-

marks=int(input("Enter your marks here:"))

if marks<30:
    grade="fail"
elif marks >= 30 < 60:
    grade="D"
elif marks >= 60 < 70:
    grade="C"
elif marks >=70 < 80:
    grade="B"
elif marks >= 80 <90:
    grade="B+"
elif marks >=90 < 95:
    grade="A"
else:
    grade="A+"
print(grade)    
