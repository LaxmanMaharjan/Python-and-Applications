"""
Everything you enter from console is string.
Don't think it is integer or float implicitly
"""
age = input("Enter your age:")
print(type(age))
print(f"you have live {int(age)*12} months")