def decorated_by(fxn):
        fxn.__doc__+='\n Decorated by decorated_by.'
        return fxn
def add(x,y):
    "Returns sum of x and y"
    return x+y

add = decorated_by(add)
help(add)

#using @syntax
@decorated_by
def subtract(x,y):
    "Returns difference of x and y"
    return x-y
help(subtract)