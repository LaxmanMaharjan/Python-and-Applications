"""
A set is created by placing all the items (elements) inside curly braces {} , separated by comma,
 or by using the built-in set() function.
It can have any number of items and they may be of different types (integer, float, tuple, string etc.)
"""

"""
Defination of Set
A set can be created in two ways. First, you can define a set with the built-in set() function:
x = set(<iter>)
argument <iter>  is an iterable. eg : list,tuple
"""
# 1.Using set()
s = set([1,2,3])
print(s)

# 2.Using Curly Braces x = {<obj>, <obj>, ..., <obj>}
# When a set is defined this way, each <obj> becomes a distinct element of the set, even if it is an iterable.
# This behavior is similar to that of the .append() list method

x = {'laxman','ram','shyam','hari','ram'}
print(x)

y = set('laxman')
print(y)

#observe the difference between print(x) and print(y)


x = set()
print(type(x))

y = {}
print(type(y))

#here x is set but y is dict

#An empty set is falsy in Boolean context:
x = set()
print(bool(x))
print(x and 1)

#The elements in a set can be objects of different types:
x = {42, 'foo', 3.14159, None}


#Don’t forget that set elements must be immutable. For example, a tuple may be included in a set:
x = {42, 'foo', (1, 2, 3), 3.14159}

#but list and dictionaries can't be the elements of set since they are mutable
a = [1,2,3,4]
#x={a}  #Error

#Operation(method ) and operator used in set

x = {1,2,3,4,5}
y = {4,5,6,7,8}

#1.Union
print(x.union(y)) # Using method
print(x | y) # Using operator

#2.Intersection
print(x.intersection(y)) # Using method, can have one or more argument
print(x & y)

#3.Difference

print(x.difference(y))
print(x - y)


#4.isdisjoint
print(x.isdisjoint(y))

#5. issubset
print(x.issubset(y))
print(x <= y)