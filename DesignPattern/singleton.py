"""This is example of use of Singleton Design pattern """
class Captain:
    _instance = None
    cap_name = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance,cls):
            cls._instance = super(Captain,cls).__new__(cls,*args,**kwargs)
        return cls._instance

    def elect_captain(self):
        if self.cap_name == None:
            self.cap_name = input("Enter the Name of captain to be elected:")
        else:
            print("Your Team captain is already elected.")
            self.get_captain()

    def get_captain(self):
        print(f"Your Team Captain is {self.cap_name}.")

print("----"*20)
print("Using c1 captain instance")
c1 = Captain()
c1.elect_captain()

print("----"*20)
print("Using c2 captain instance")
c2 = Captain()
c2.elect_captain()

print("----"*20)
if c1 == c2:
    print("c1 and c2 are same captain instances")
else:
    print("c1 and c2 are not same captain instances")
