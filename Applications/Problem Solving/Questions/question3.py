string = "l adore it"
a = string[0]
words = string.split()
w = ''
l = 0
for word in words:
    if len(word)>l:
        w = word
        l = len(word)

print(w,l)

index = words.index(w)
words.remove(w)

new_words = []
for word in words:
    count = l-len(word)
    new_word = a*count + word
    new_words.append(new_word)

new_words.insert(index,w)
print(new_words)
print(" ".join(new_words))
