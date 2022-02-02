x=3
y=4
z=6
print("Max num:",x if x>y>z else y if y>z else z)
print("Min num:",x if x<y<z else y if y<z else z)

print(input("Enter any value").split(','))
print(f"Value of x:{x}\nValue of y:{y}")

x,y,z= [5,6,7]
print(x,y,z)