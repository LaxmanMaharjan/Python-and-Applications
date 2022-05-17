"""
Write a program that takes a number of multiple digits as an input and calculates the sum of products of digits at symmetric positions.If there's odd number of digits, the middle digit should be added as it is. If the result is greater that a single digit number, repeat the same process until you get a single number. Print the final single digit number as output.

Example:
    Input: 101
    Output: (1*1)+0 = 1
"""

def solution(number):
    string = str(number)
    half = int(len(string)/2)
    result = 0
    old_flag = True

    if len(string) % 2 == 0:  # even
        first_str = string[:half]
        second_str = string[half:]
        old_flag = False
    else:  # odd
        first_str = string[:half]
        second_str = string[half+1:]

    for i in range(half):
        result += int(first_str[i])*int(second_str[i])

    if old_flag:
        result += int(string[half])

    return result



    
