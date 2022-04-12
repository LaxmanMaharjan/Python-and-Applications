"""
Decorator pattern is a structural pattern that allows adding new behaviors to
objects dynamically by placing them inside special wrapper objects.
"""
from abc import ABC,abstractmethod
class Component(ABC):
    """
       The base Component interface defines function (makeHouse in the case) that can be altered by
       decorators.
       """
    @abstractmethod
    def makeHouse(self):
        pass

class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """
    def __init__(self):
        self.component = ConcreteComponent()

    def makeHouse(self):
        self.component.makeHouse()

class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations (makeHouse in the case). There
    might be several variations of these classes.
    """
    def makeHouse(self):
        print("Original is Complete.\nIt is closed for modification.")

class FloorDecorator(Decorator):
    """This is concrete Decorator to wrap the additional function to makeHouse"""
    def makeHouse(self):
        super().makeHouse()
        print("*" * 10, "Flooring Process", '*' * 10)
        self.floorHouse()
        print("Flooring Process completed.")
    def floorHouse(self):
        print("Now I am adding floor on the top of the house.")

class PaintDecorator(Decorator):
    """This is concrete Decorator to wrap the additional function to makeHouse"""
    def makeHouse(self):
        super().makeHouse()
        print("*" * 10, "Painting Process", '*' * 10)
        self.paintHouse()
        print("Painting Process completed.")
    def paintHouse(self):
        print("Now I am painting the house.")

print("*" * 10, "Decorator Pattern Demo", '*' * 10)
print("-"*40)
print("*" * 10, "Paint Decorator", '*' * 10)
p = PaintDecorator()
p.makeHouse()
print("-"*40)
print("*" * 10, "Paint Decorator", '*' * 10)
f = FloorDecorator()
f.makeHouse()