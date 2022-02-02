class student:
    """ This class is for demo purpose """
    def __init__(self,name,rollno):
        print(f"Address of self = {id(self)}")
        self.name = name
        self.rollno = rollno

    def get_info(self):
        print(f"Student's name:{self.name}")
        print(f"Student's rollno:{self.rollno}")

s = student("laxman",100)
print(f"Address of Student's refrence variable = {id(s)}")
print('-'*20)
s.get_info()
