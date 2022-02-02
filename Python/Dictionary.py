people = {
    'fname': 'Joe',
    'lname': 'Fonebone',
    'age': 51,
    'spouse': 'Edna',
    'children': ['Ralph', 'Betty', 'Joey'],
    'pets': {'dog': 'Fido', 'cat': 'Sox'}
    'married':True
    'children':None
    }
def printing(dictionary):
    """
    This function prints all the key-values from dictionary in list of tuple
    :return:
    """
    for i in list(dictionary.items()):
        print(i)

#adding an entry to the existing dictionary

people['friends'] = ('Rahul','Aman','Sarah')
printing(people)

#Retrieving value from dictionary
print(people['fname'])

#Operator in Dictionary
print('fname' in people) #looks for key

#built in function for dictionary
print(people.get('fname'))

#d.items returns a list of tuple of key-value pair
print(people.items())

# d.keys() -> returns a list of all keys in dict
print(people.keys())

#d.values() -> returns a list of all values in dict
print(list(people.values()))

#d.pop(<key>) -> removes a key from a dictionary
people.pop('fname')
print(people)
#d.popitem -> removes a key-value pair from dictionary
people.popitem()
print(people)

#d.update(<obj>)

d1 = { 'a':10,'b':20,'c':30}

d2={'b':200,'d':40}

d1.update(d2)
print(d1)

for x,y in people:
    print(x,y)