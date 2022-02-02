"""
This program domonstrates the order of application of decorator in nested decorators
"""
def also_decorated_by(fxn):
    fxn.__doc__ += "\nDecorated by also_decorated_by"
    return fxn
def decorated_by(fxn):
    fxn.__doc__ += "\nDecorated by decorated_by"
    return fxn
@also_decorated_by
@decorated_by
def add(x,y):
    "Returns the sum of x and y"
    return x+y

help(add)