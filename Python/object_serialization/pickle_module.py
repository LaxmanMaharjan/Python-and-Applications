"""
Object serialization is done to convert python object to the form that could be saved in the file
or that could be used to send python object when requested by other app like javascript app,andriod app etc.
"""
import pickle
class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee id:{self.id}\nEmployee Name:{self.name}\nEmployee salary:{self.salary}")

e = Employee(101,"anna",1500)

with open("pickling.txt",'wb') as file:
    #serialization or pickling process
    pickle.dump(e,file) #dump function converts object to byte string and stores it in file

with open ("pickling.txt",'rb') as file:
    #Deserialization or unpickling process
    loaded_obj = pickle.load(file)

loaded_obj.display()
converted = pickle.dumps(e)
print(converted)
loaded_obj1 = pickle.loads(converted)
print(loaded_obj1.__class__.__name__)
