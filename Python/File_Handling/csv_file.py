import csv
#writing into csv file
# with open('emp.csv','a',newline='') as file:
#     w = csv.writer(file)
#     w.writerow(['ENO','ENAME','ESAL','EADDR'])
#     n = int(input("Enter the no. of Employee:"))
#     for i in range(n):
#         eno = input("Enter Employee No.:")
#         ename = input("Enter Employee Name:")
#         esal = input("Enter Employee salary:")
#         eaddr = input("Enter Employee Address:")
#         w.writerow([eno,ename,esal,eaddr])

#Reading from csv file
with open('emp.csv','r') as file:
    r = list(csv.reader(file))
    print(r)