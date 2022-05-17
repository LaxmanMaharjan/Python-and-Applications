#Write a program that takes a string as an input and prints it after removing all consecutive occurences of repeated character that is non-vowel.

# Examples:
# Input : Hello my fellow peeps
# Output : Helo my felow peeps

vowels = "AEIOUaeiou"

def remove_consecutive_duplicates(s):
    new_s = ""
    prev = ""
    for char in s:
        if len(new_s) == 0:
            new_s += char
            prev += char

        if char == prev and (char not in vowels):
            continue

        else:
            new_s += char
            prev = char

    return new_s

string = "Hello my fellow peeps"
print(remove_consecutive_duplicates(string))
