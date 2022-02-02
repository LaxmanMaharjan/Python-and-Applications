def file_property(filename):
    with open(f"{filename}",'r+') as file:
        print(f"File Name:{file.name}")
        print(f"File Mode:{file.mode}")
        print(f"Is file Readable:{file.readable()}")
        print(f"Is file Writable:{file.writable()}")
        print(f"Is file closed:{file.close()}")


# with open('testfile.txt','r+') as file:
#     line = file.readline()
#     while line:
#         print(line,end='')
#         line = file.readline()

# with open("testfile.txt",'r+') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line,end='')
