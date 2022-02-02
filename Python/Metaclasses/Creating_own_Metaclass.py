"""
Learning how to create a metaclass

"""
class example:
    pass
e = example()
class Meta(type):
    "A custom metaclass that add no functionality"
    def __new__(cls, name, bases, attrs):
        return super(Meta,cls).__new__(cls, name, bases, attrs)

#This Meta metaclass can be used as metaclass to create an object like type metaclass

C = Meta('C',(),{})

print(type(C))
print(type(example))
print(type(e))

"""
Another way of declaring metaclass is shown in use_of_metaclass file

"""