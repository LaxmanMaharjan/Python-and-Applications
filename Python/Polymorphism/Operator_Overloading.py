"""
The purpose of these so-called “magic methods” is to overload Python operators or built-in
methods.

"""
class Polynomial:
    def __init__(self,*args):
        self.coeffs = args

    def __add__(self, other): #overloading +
        return Polynomial(*(x+y for x,y in zip(self.coeffs,other.coeffs)))

    def __sub__(self, other): #overloading -
        return Polynomial(*(x-y for x,y in zip(self.coeffs,other.coeffs)))

    def __iadd__(self, other):  #overloading +=
        return Polynomial(*(x+y for x,y in zip(self.coeffs,other.coeffs)))

    def __isub__(self, other): #overloading -=
        return Polynomial(*(x-y for x,y in zip(self.coeffs,other.coeffs)))

    def __eq__(self, other):  #overloading ==
        if self.coeffs == other.coeffs:
            return True
        else:
            return False

    def __str__(self): #it is invoked when print on the polynomial type is called
        return f"Poynomial*{self.coeffs}"

p1 = Polynomial(1,2,3) #x^2 + 2x + 3
p2 = Polynomial(1,2,3) #x^2 + 2x + 3
p3 = p1 + p2

print(p1 + p2 + p3)