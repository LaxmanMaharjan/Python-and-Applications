"""
Getters and Setters like in c++
"""
class House:
    def __init__(self):
        self.__price = 0

    def set_price(self,price):
        if price > 0 :
            self.__price=price

    def get_price(self):
        return self.__price

#
# h = House()
# h.set_price(10)
# result = h.get_price()
# print(result)

"""
Using Property Decorator's setter,getter and deleter to validate the value of attribute of the class
validating if it's positive number or not
"""
class House1:
    def __init__(self,new_price):
        self.price = new_price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        if (new_price > 0):
            self._price = new_price
        else:
            print("Invalid Price")
    @price.deleter
    def price(self):
        del self._price
h = House1(10)

