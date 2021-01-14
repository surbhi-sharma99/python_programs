class Img():

    #attributes
    #real part
    # imagnary part

    def _init_(self,real,imaginary):

        self.real = flaot(real)

        self.img = float(imaginary)


        #behaviours

             #representention function
    def _repr_(self):

        presntation = str(self.real)+ str(self.imaginary)+"i"
            
        return presntation

    def _add_(self, another):

        real = self.real+ another.real

        img = sel.img + another.img

        return Img(real, img)

        
        
             #addition
             #subtraction
             #amplitude
             #getters: get some value of attribute
             #setters:set some value of attribute

a = Img(10, 15)

b = Img(20,29)

c=  a+b
