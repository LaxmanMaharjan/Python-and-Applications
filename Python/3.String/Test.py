def Reverse(value):
    reverse = ''
    i = len(value) - 1
    while i>=0:
        reverse += value[i]
        i -=1
    print(int(reverse))
T = int(input("Enter the value of T:"))
for _ in range(T):
     Reverse(input("Enter the value:"))