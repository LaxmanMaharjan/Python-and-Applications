class Polynomial:
    def __init__(self,*coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return f"Polynomial(*{self.coeffs})"

    def __add__(self, other):
        return Polynomial(*(x+y for x,y in zip(self.coeffs,other.coeffs)))

    def __len__(self):
        return (len(self.coeffs) - 1)

    def __iter__(self):
        return iter(self.coeffs)

    def add(self,other):
        return Polynomial(*(x+y for x,y in zip(self.coeffs,other.coeffs)))
p1 = Polynomial("laxman","ram","shyam")
p2 = Polynomial(1,2,3)
for i in p1:
    print(i)

#p3 = p1+p2
print(p1)
print(p2)
print(len(p1))



#print(p1.add(p2))