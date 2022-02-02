#Exception handling with try-exception block
print("Hello")
try:
    print(10/0)
except ZeroDivisionError as msg:
    print(f"Error:{msg}")
    print(f"Exception class:{type(msg)}")
    print(f"Alternate method for Exception class:{msg.__class__}")
    print(f"Name of Exception class:{msg.__class__.__name__}")
print("World")
