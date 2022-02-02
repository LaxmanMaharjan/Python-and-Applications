people_list = ['Ram\n','laxman\n','shyam\n']
with open('writing.txt','w') as file:
    file.write("demo\nwrite\n")
    file.writelines(people_list)