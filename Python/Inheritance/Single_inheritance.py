"""
These Class is being built for demo of Method Resolution Order (MRO) and
Super() function

"""

"""
This is demonstration of MRO 
"""
class Mother:
    def __init__(self):
        print(f"Displaying from {self.__class__}")

    def __repr__(self):
        return "Mother"

    def display(self):
        print(f"Displaying display method from {self.__class__}")
class Son(Mother):
    def __init__(self):
        print(f"Displaying from {self.__class__}")
    def display(self):
        print(f"Displaying display method from {self.__class__}")

s = Son()
s.display()
print(Son.mro())

print("---"*20)
"""
This is the demonstration of Super()
"""

class Father:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Father"

    def display(self):
        print(f"Displaying from {self.__class__}")
        print(f"Name:{self.name}\nAge:{self.age}")

class Child(Father):
    def __init__(self,name,age,qualification):
        super().__init__(name,age)
        self.qualification = qualification

    def display(self):
        super().display()
        print(f"Qualification:{self.qualification}")
c = Child("laxman",21,"+2")
c.display()
print(isinstance(c,Child))
print(type(Child))