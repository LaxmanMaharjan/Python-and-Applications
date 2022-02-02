"""
How to access member of one class from another class

"""
class Employee:
    def __init__(self,name,id,salary):
            self.name = name
            self.id = id
            self.salary = salary

    def display(self):
            print(f"Name:{self.name}\nId:{self.id}\nSalary:{self.salary}")

class Test:
    @staticmethod
    def bonus_salary(emp,bonus):
        emp.salary +=bonus
        emp.display()
emp = Employee("Ram",1,1000)
Test.bonus_salary(emp,1000)