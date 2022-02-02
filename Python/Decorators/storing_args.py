import functools
import pickle
# store ={}
#
# def add1(*args):
#      if args in store:
#          print("Returning from stored value.")
#          return store[args]
#      else:
#          result = 0
#          for i in args:
#              result+=i
#          store[args]= result
#          print("Returning by calculation.")
#          return result
#

#Writing it using decorator
# def memoize(fxn):
#     cache = {}
#     functools.wraps(fxn)
#     def wrapper(*args,**kwargs):
#         if args in cache:
#             print("Returning from stored value.")
#             return cache[(args,tuple(kwargs.values()))]
#         else:
#             print("Returning from Calculation.")
#             cache[(args,tuple(kwargs.values()))] = fxn(*args,**kwargs)
#             return cache[(args,tuple(kwargs.values()))]
#     return wrapper

#using pickle for dictionary key
def memoize(fxn):
    cache = {}
    functools.wraps(fxn)
    def wrapper(*args,**kwargs):
        t = (pickle.dumps(args),pickle.dumps(kwargs))
        if t in cache:
            print("Returning from stored value.")
            return cache[t]
        else:
            print("Returning from Calculation.")
            cache[t] = fxn(*args,**kwargs)
            return cache[t]
    return wrapper

@memoize
def add(*args,**kwargs):
    sum = 0
    #sum = functools.reduce(lambda x, y: x + y, list(args) + list(kwargs.values()))
    for i in list(args)+list(kwargs.values()):
        sum += i
    return sum

print(add(2,2,x=2))
print(add(2,2))
