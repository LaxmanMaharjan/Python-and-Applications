"""
Understanding the asterisk(*) of Python
There are 4 cases for using the asterisk in Python.
1.For multiplication and power operations.
2.For repeatedly extending the list-type containers.
3.For using the variadic arguments. (so-called “packing”)
4.For unpacking the containers.
"""

"""
1.For multiplication and power operations.
"""
print(2*3) #answer = 6
print(2**3) #answer = 8

primes = [2, 3, 5, 7, 11, 13]

def numbers(*num):
    print(num)
    print(type(num))
numbers(*primes)