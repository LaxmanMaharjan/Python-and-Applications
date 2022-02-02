"""
Higher order Function
It takes a funtion as argument and returns function

"""
"""
Example 1
Closure property in python
"""
from time import time
user ={
    'username':'laxman',
    'password':123
}

def user_info(function):
    def test(username):
        if user['username'] == username:
            return function(username)
    return test

def func(username):
    return f"password of {username} = {user['password']}"

returned_function = user_info(func)
print(returned_function.__name__)
print(returned_function("laxman"))

"""
Example 2
"""
def timer(func):
    def wrapper(*args,**kwargs):
        before = time()
        ans = func(*args,**kwargs)
        after = time()
        print("time is:",after-before)
        return ans
    return wrapper

def add(x,y):
    return x+y

add = timer(add)
"""
Using decorator in pyton simply replace the code add=timer(add)
by using @timer in the top of add
"""
rv = add(3,4)
print(rv)


def practice(func1):
    def wrapper(x,y):
        print("This function can be wrapped with some functionality")
        ans = func1(x,y)
        return ans
    return wrapper
@practice
def subtract(x,y):
    return x+y



print(subtract(5,3))
