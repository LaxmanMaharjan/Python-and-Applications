try:
    x = int(input("Enter first Number:"))
    y = int(input("Enter second number:"))
    print(x/y)
except ZeroDivisionError as msg:
    print("can't divide by zero")
except ValueError as msg:
    print("Please provide integer value.")
