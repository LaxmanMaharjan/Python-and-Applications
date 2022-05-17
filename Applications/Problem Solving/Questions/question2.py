string = "{{{{((()}}"
count = string.count("{")-string.count("}")+string.count("(")-string.count(')')
print(count)
