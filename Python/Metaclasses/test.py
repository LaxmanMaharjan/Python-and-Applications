from Codes.Metaclasses.meta_coding import Logged
class Myclass(metaclass=Logged):
    def foo(self):
        pass
myobject = Myclass()
myobject.foo()