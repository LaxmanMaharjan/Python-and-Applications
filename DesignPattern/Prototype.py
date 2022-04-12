import random
from abc import ABCMeta, abstractmethod
from copy import deepcopy
class BasicCar(metaclass=ABCMeta):
    model_name = None
    base_price = None
    on_road_price = None

    def set_modelname(self,name):
        self.model_name = name

    def get_modelname(self):
        return self.model_name

    def set_additionalprice(self):
        return random.randint(500,1000)

    @abstractmethod
    def clone(self):
        pass

class Nano(BasicCar):
    def __init__(self,modelname):
        self.model_name = modelname

    def __str__(self):
        return f"Car is {self.model_name} and Price is {self.base_price} and On Road Price is {self.on_road_price}"

    def clone(self):
        return deepcopy(self)

class Ford(BasicCar):
    def __init__(self,modelname):
        self.model_name = modelname

    def __str__(self):
        return f"Car is {self.model_name} and Price is {self.base_price} and On Road Price is {self.on_road_price}"

    def clone(self):
        return deepcopy(self)


nano = Nano("Green Nano")
nano.base_price = 100000

ford = Ford("Yellow Ford")
ford.base_price = 500000

new_nano = nano.clone()
new_nano.on_road_price = new_nano.base_price + new_nano.set_additionalprice()

new_ford = ford.clone()
new_ford.on_road_price = new_ford.base_price + new_ford.set_additionalprice()

print("----"*20)
print(nano)
print(ford)

print("----"*20)
print("new_ford Cloned from nano which is instance of class Nano with on_road_price as additional info.")
print(new_nano)

print("----"*20)
print("new_ford Cloned from ford which is instance of class Ford with on_road_price as additional info.")
print(new_ford)
print("----"*20)


