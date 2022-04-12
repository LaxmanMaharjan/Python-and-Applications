class Rectangle:
        def __init__(self,length,width):
                self.length = length
                self.width = width

class Triangle:
        def __init__(self,width,height):
                self.width = width
                self.height = height

class Calculator:
        def get_area(self,Rect):
                return Rect.length * Rect.width

class CalculatorAdapter:
        def get_area(self,triangle):
                rect = Rectangle(None,None)
                rect.length = triangle.width
                rect.width = triangle.height * 0.5
                c = Calculator()
                return c.get_area(rect)

 
print("**"*20,"Adapter Pattern Demo", "**"*20)
calAdapter = CalculatorAdapter()
t = Triangle(20,10)
print(f"Area of Triangle is {calAdapter.get_area(t)} square")
