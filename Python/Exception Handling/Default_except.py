"""
Default Except is executed when all other except block is not executed.
Default except must be always as last.
"""
try:
    x = int(input("Enter first num:"))
    y = int(input("Enter second num:"))
    print(x/y)
except ZeroDivisionError as msg:
    print("can't divide by zero.")
except:
    print("Please enter the valid input.")
