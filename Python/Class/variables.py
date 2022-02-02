class Student:
    """
    This class is for the purpose of learning different types of variable in class
    and different types of function in class
    """
    College_name = "Khowpa College of Engineering" # class variable/static variable
    def __init__(self,name,rollno):
        self.name = name # self.name is instance variable
        self.rollno = rollno #self.rollno is instance variable

    def get_address(self):
        """
        self.address is instance variable declared from instance method
        not from __init__ method
        self.address is created only if get_address method is called
        :return:
        """
        self.address = input("Enter you address:")

    def get_info(self):
        print(f"Name:{self.name}\nRollno:{self.rollno}\nAddress:{self.address}")

    @classmethod
    def modify_class_variable(cls):
        cls.College_name = input("Enter the college name:")


s = Student("Ram",1)
s.x = "string"  # Creating instance variable from outside of the class from reference variable
print(s.College_name)
#s.modify_class_variable()
print(s.College_name)
s1 = Student("laxman",2)
print(s1.College_name)



