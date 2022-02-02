numbers = list(range(10))
doubled_numbers = [2*i for i in numbers]
phrases = [f"you are {age} years old" for age in numbers]
evens = [i for i in numbers if i%2 == 0]
print(evens)

names = ["laxman","ram","shyam"]

capital_names = [i.upper() for i in names]
print(capital_names)

print(names[1:])