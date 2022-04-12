from abc import ABC,abstractmethod
class RectInterface(ABC):
	@abstractmethod
	def get_area(self,length,width):pass
	@abstractmethod
	def about_Rectangle(self):pass

class TriInterface(ABC):
	@abstractmethod
	def get_area(self,width,height):pass
	@abstractmethod
	def about_Triangle(self):pass
	
class Rectangle(RectInterface):
	def __init__(self,length,width):
		self.length = length
		self.width = width
	def about_Rectangle(self):
		print(f"Rectangle with length:{self.length} and width: {self.width}")
		
	def get_area(self):
		return self.length * self.width

class Triangle:
	def __init__(self,base,height):
		self.base = base
		self.height = height

	def about_triangle(self):
		print(f"Triangle with base:{self.base} and height: {self.height}")
	
	def get_area(self):
		return 0.5 * self.base * self.height
 
print("*"*20," Modified Adapter Pattern Demo", "*"*20)

t = Triangle(10, 5)
print(f"Area of Triangle is {t.get_area()} square")
