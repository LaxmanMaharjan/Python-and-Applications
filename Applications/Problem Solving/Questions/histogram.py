fruits = ['apple','orange','grapes']
def histogram(fruit):
    result={}
    for i in fruit:
        if i not in result.keys():
            result[i]=1
        else:
            result[i]= result[i]+ 1
    return result
for fruit in fruits:
    print(histogram(fruit))

