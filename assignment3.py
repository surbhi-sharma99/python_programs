#assignment 3:-

marks_maths = int(input("Enter marks of maths"))
marks_science = int(input("Enter marks of science"))
marks_english = int(input("Enter marks of English"))

per=(marks_maths+marks_science+marks_english)/3

if per>=95:
    grade="A+"
    result="pass"
elif per>=90:
    grade="A"
    result="pass"
elif per>=80:
    grade="B+"
    result="pass"
elif per>=75:
    grade="B"
    result="pass"
elif per>=65:
    grade="C+"
    result="pass"
elif per>=50:
    grade="D"
    result="pass"
else:
    grade="E"
    result="fail"
print("You have " + result + ",with grade:"+grade)    
    
