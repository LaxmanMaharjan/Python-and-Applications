"""
Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.
"""
str = "tact coa"
def check(str):
    count = {}
    for i in str:
        if i == ' ':
            continue
        else:
            if i not in count.keys():
                count[i] = 1
            else:
                count[i] += 1
    count_odd = 0
    for i in count.values():
        if i%2 != 0:
            count_odd += 1
    if count_odd == 1:
        return True
    else:
        return False
print(check(str))