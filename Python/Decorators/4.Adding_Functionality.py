"""
Sometimes you want additional functionality to run when the decorated method is
executed.
"""
def requires_int(fxn):
    """
    decorator that ensures that every argument the function receives is an integer, and
    complains otherwise:
    :param fxn:
    :return:
    """
    def inner(*args,**kwargs):
        values_lists = list(kwargs.values())
        for arg in list(args)+values_lists:
            if not isinstance(arg,int):
                raise TypeError(f"{fxn.__name__} only accepts integer argument")
        return fxn(*args,**kwargs)
    return inner

@requires_int
def add(x,y):
    "Return the sum of x and y"
    return x+y

#print(add(3,"f"))
help(add)

