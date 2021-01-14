"""
from student_managemenet import Student

student_name = "ugu,idb,i,sdb,vie,ibid,bvibv,ikdfb,vkbfi,kbefkv,bkfdbv,vkffb,vkfdb,vvki,dfv".split(",")

students = []
for i in range(len(student_name)):

	students.append( Student(i + 1, student_name[i]) )


for stu in students:

	print(stu)

"""
from student_managemenet import Complex


a = Complex(10, 70)
b = Complex(5, 10)


print(a)
print(b)

a_plus_b = a + b

print(a_plus_b)