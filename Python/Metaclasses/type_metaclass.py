"""
Creating a class using normal way
"""
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        pass

    def sleep(self):
        pass

class Cat(Animal):
    def meow(self):
        pass
"""
Creating a Class using type
"""

def init(self,name):
    self.name = name

def eat(self):
    pass

def sleep(self):
    pass

Animal1 = type('Animal1',(),{
    '__doc__':"Animal1 is the class created by type",
    '__init__':init,
    'eat':eat,
    'sleep':sleep
})

"""
It has a couple of differences, most notably that this code leaves functions called init,
eat, and go_to_vet, unattached to the class, in that namespace.
"""

def meow(self):
    pass
Cat1 = type('Cat1',(Animal1,),{'meow':meow})
print(Cat1.__dict__)

a = Animal1("Feuri")
print(a.name)