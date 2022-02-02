with open("testfile.txt",'w') as file:
    #print(file.read())
    print(file.tell())
    file.seek(5,0)
    #print(file.tell())
    file.write("usingseek")