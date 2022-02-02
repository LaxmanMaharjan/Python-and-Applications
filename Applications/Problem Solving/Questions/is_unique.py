"""
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""
string = "laxmanmaharjan"
unique = ''
for i in string:
    if i not in unique:
        unique += i
print(unique)

string = "My name is Laxman Maharjan."
new_string = ''

for i in string:
    if i == ' ':
        new_string += '%20'
    else:
        new_string += i
print(new_string)
