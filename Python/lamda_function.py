from functools import reduce
numbers = list(range(10))
words = "my name is laxman maharjan"
vowels = ['a','e','i','o','u']

#Using filter() function

print(list(filter(lambda x: x in vowels ,words))) # one liner check_vowel

def check_vowels(word):
    catched_vowels = []
    for i in word:
        if i in vowels:
            catched_vowels.append(i)
    return catched_vowels
print(check_vowels(words))

#map() applies a function to all the items in an input_list
squared_number = list(map(lambda x:x*x , numbers))

print(squared_number)

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply,add]
for i in range(5):
    result = list(map(lambda x:x(i),funcs))
    print(result)

#using reduce()
#example products of list of integers
#normal approach
product = 1
numbers1 = range(1,5)
for num in numbers1:
    product *=num
print(f"product is {product}")

#using reduce function from functools
product = reduce(lambda x,y:x*y , numbers1)
print(product)