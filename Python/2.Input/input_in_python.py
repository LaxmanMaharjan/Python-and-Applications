def own_split(variable,seperator):
    spilted = []
    count = 0
    start_index = 0
    end_index = 0
    count_sep = 0
    for i in variable:
        if i == seperator:
            count_sep += 1
    for i in variable:
        if i == seperator:
            if start_index == 0 and end_index == 0:
                end_index = count
                spilted.append(variable[start_index:end_index])
            # elif start_index == 0 and end_index != 0:
            #     start_index = end_index+1
            #     end_index = count
            #     spilted.append(variable[start_index:end_index])
            # elif start_index != 0 and end_index != 0:
            #     start_index = end_index+1
            #     end_index = count
            #     spilted.append(variable[start_index:end_index])
            else:
                start_index = end_index+1
                end_index = count
                spilted.append(variable[start_index:end_index])
        elif len(spilted) == count_sep:
            spilted.append(variable[count:len(variable)])
            break
        count+=1
    return spilted
print(own_split(input("Enter any string:"),' '))
