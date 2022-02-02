string = 'laxman'
print(''.join(reversed(string)))

print(string[::-1])

#3rd method
reverse = ''
print(v)
print(id(reverse))
i = len(string)-1
while i>=0:
    reverse += string[i]
    print(id(reverse))
    i -=1
print(reverse)