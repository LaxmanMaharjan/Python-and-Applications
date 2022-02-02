"""
An iterator is an object that can be iterated upon,
meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__() .
"""
class PowTwo:
    def __init__(self,max=0):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if (self.num < self.max):
            result = 2 ** self.num #2 ^ self.num
            self.num += 1
            return result
        else:
            raise StopIteration

for i in PowTwo(4):
    print (i)
