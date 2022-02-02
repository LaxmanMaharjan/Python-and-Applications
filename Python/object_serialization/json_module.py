"""
You can convert built in objects like dictionart,lists,tuples to json strings but you can't convert user defined object
or any other complex objects. For this we have to do some extra stuffs
"""
import json
people = {
    'fname': 'Joe',
    'lname': 'Fonebone',
    'age': 51,
    'spouse': 'Edna',
    'children': ['Ralph', 'Betty', 'Joey'],
    'pets': {'dog': 'Fido', 'cat': 'Sox'},
    'married':True,
    'girlfriend':None
    }
#serialization process
with open("jsoning.json",'w') as file:
    json.dump(people,file,indent=4)
#Deserialization process
with open("jsoning.json",'r') as file:
    obj = json.load(file)
print(obj)

#Serialization process
json_string = json.dumps(people)
print(type(json_string))

dictionary = json.loads(json_string)
print(type(dictionary))
