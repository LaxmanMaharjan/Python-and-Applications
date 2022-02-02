"""
This Program helps to preserve the doc string and indentity of the function
"""
import functools
def requires_int(fxn):
    """
    decorator that ensures that every argument the function receives is an integer, and
    complains otherwise:
    :param fxn:
    :return:
    """
    @functools.wraps(fxn)
    def inner(*args,**kwargs):
        values_lists = list(kwargs.values())
        for arg in list(args)+values_lists:
            if not isinstance(arg,int):
                raise TypeError(f"{fxn.__name__} only accepts integer argument")
        return fxn(*args,**kwargs)
    return inner

@requires_int
def add(x,y):
    "Return the sum of x and y.Here the arguments must be integer."
    return x+y
help(add)
