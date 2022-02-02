#Set comprehension is same as list comprehension only the {} is used instead of []

names = ["laxman","Ram","Shyam"]
surnames = ["Maharjan","RAi","Bhandari"]

fullnames =  { f"{x} {y}" for x,y in zip(names,surnames) }
print(fullnames)

capitalized_fullnames = {x.upper() for x in set(names) | set(surnames)}
print(capitalized_fullnames)

fullnames1 = {names[i]:surnames[i] for i in range(len(names))}
print(fullnames1)