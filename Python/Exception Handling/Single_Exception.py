"""
This demonstrate the single except that can handle multiple exception.
This should be used when single can deal with multiple exception.
"""

try:
    x = int(input("Enter first num:"))
    y = int(input("Enter second num:"))
    print(x/y)
except (ValueError, ZeroDivisionError) as msg:
    print("Please enter valid input")
    print(msg.__class__.__name__)