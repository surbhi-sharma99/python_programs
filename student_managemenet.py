class Student():

	#properties, attendance, marks_maths, marks_science, roll_no
	def __init__(self, roll_no, full_name ):

		self.roll_no = roll_no
		self.name    = full_name
		self.attendance = 0
		self.marks_science = 0
		self.marks_maths = 0

	def __repr__(self):

		intro = "I am roll no " + str(self.roll_no) + " with name : " +  self.name
		return intro
		

	#behaviours
	def inc_attendance(self):

		self.attendance = self.attendance + 1

	def update_marks_maths(self, marks):

		self.marks_maths = marks

	def get_roll_number(self):

		return self.roll_number



class Complex():

	def __init__(self, real, imgaginary):

		self.real = real
		self.img  = imgaginary

	def __repr__(self):

		return str(self.real) + " + i" + str(self.img)

	def __add__(self, another_no):

		real_part_sum = self.real + another_no.real
		img_part_sum  = self.img  + another_no.img

		return Complex(real_part_sum, img_part_sum)



