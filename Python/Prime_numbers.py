def prime_numbers(x1,x2):
    for i in range(x1,x2):
        num = 1
        for j in range(2,i):
            if i%j == 0:
                num +=1
                print(f"/n {num} of {i}")
                break
        if num == 1 and i!=1:
            print(f'{i} is prime')

#without using num variable
def prime(x1,x2):
    for i in range(x1, x2):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            if i!=1:
                print(f"{i} is a prime")

prime(1,100)
