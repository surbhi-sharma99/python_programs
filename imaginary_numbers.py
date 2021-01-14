from math import sqrt
print(__name__)

class Img():

	#attributes
		#real part
		#imaginary part
	def __init__(self, real, imaginary):

		self.real = float( real )
		self.img  = float( imaginary )

	#behaviours

		#representation function
	def __repr__(self):
		presentation = str( self.real ) + " " + str( self.img ) + "i"

		return presentation


	def __add__(self, another):

		if another.__class__ == Img:
			real = self.real + another.real
			img  = self.img  + another.img

		else:
			real = self.real + another
			img  = self.img


		return Img(real, img)

	def __sub__(self, another):

		return Img( self.real - another.real, self.img - another.img )


	def __abs__(self):

		return sqrt(self.real**2 + self.img**2)


if __name__ == "__main__":

	a = Img(100, 15)
	b = Img(12, 89)

	c = a + b

	print( c )
	print( abs(c) )
