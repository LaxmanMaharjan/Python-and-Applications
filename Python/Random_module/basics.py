numbers=[1,7,5,9,2,12,3]
k=2
answers = []

for i in numbers:
    for j in numbers:
        if i-j == 2:
           answers.append((i,j))
print(answers)