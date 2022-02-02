"""
generator is also  an iterator

"""

from time import sleep
def compute():
    rv = []
    for i in range(5):
        sleep(1)
        rv.append(i)
    return  rv
for i in compute():
    print(i)

def compute1():
    for i in range(5):
        sleep(1)
        yield i
for j in compute1():
    print(j)
z = compute1()
print(z)
print(type(z))

"""
Generator Expression

"""
i = (x*x for x in range(5))
print(next(i))
print(next(i))
print(next(i))

for i in (x*x for x in range(5)):
    print(i)