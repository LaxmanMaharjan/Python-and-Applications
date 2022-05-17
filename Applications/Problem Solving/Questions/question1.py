a = "  hello my name is laxman maharjan  "
left_spaces = len(a) - len(a.rstrip())
right_spaces = len(a) - len(a.lstrip())

content = a.strip().replace(" ","*").upper()
ans = " "*left_spaces + content + " "*right_spaces
print(ans)
