"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -) true
pales, pale -) true
pale, bale -) true
pale, bae -) false
"""

def check(str1,str2):
    """
    This function checks the one way.
    :param str1:
    :param str2:
    :return: bool
    """
    index = 0
    if str1 == str2:
        return True
    else:
        for i in str1 if len(str1) <= len(str2) else str2:


check("pale","ple")