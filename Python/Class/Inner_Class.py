"""
Demonstration of Inner class
when used
In a case where without existing one type of object if there is no chance of existing one type of object
then we should go for inner class

"""
class Person:
    def __init__(self,name,dd,mm,yyyy):
        self.name = name
        self.dob = self.DOB(dd,mm,yyyy)

    def display(self):
        print(f"Date of birth of {self.name}:{self.dob.get_dob()}")
    class DOB:
        def __init__(self,dd,mm,yyyy):
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

        def get_dob(self):
            return f"{self.yyyy}-{self.mm}-{self.dd}"

        def display(self):
            print(f"Date of Birth:{self.yyyy}-{self.mm}-{self.dd}")

p = Person("Laxman",2055,6,8)
p.dob.display()
