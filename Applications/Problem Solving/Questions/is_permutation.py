"""
Given two strings, write a method to decide if one is a permutation of the
other.
"""
def check_permutation(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        for i in str1:
            if i in str2:
                continue
            else:
                return False
    return True
print(check_permutation("good","dono"))